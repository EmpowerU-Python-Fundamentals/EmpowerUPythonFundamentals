import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import csv
from datetime import datetime
import logging

from config_manager import load_config, save_config, save_folders, load_folders
from db_buffer import db_buffer
from telegram_notifier import TelegramNotifier
from watchdog_handlers import MyHandler, WatcherThread

logging.basicConfig(
    filename='log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

DB_PATH = 'events.db'
FOLDERS_FILE = "folders.yaml"
CONFIG_FILE = "config.yaml"
DB_BUFFER_SIZE = 50
TREE_MAX_ROWS = 1000

class FileMonitorApp:
    """
    Головний клас додатка, що керує графічним інтерфейсом користувача
    та логікою моніторингу файлової системи.
    """
    def __init__(self, root):
    	"""
    	Ініціалізація додатку, налаштування головного вікна, завантаження конфігурації та папок для моніторингу.
        Також створюється об'єкт для відправки повідомлень у Telegram та ініціалізуються змінні для фільтру подій.
        """
        self.root = root
        self.root.title("Моніторинг файлової системи")
        self.config = load_config()
        self.paths = load_folders() or self.config.get('paths', [])
        self.thread = None
        self.notifier = TelegramNotifier(
            self.config.get('telegram',{}).get('token',''),
            self.config.get('telegram',{}).get('chat_id','')
        )
        self.event_filter = set(self.config.get('events',['created','modified','deleted','moved']))
        self._all_events = []
        self._build_ui()
        for p in self.paths:
            self.lst.insert("end", p)

    def _build_ui(self):
    	"""
        Приватний метод для побудови всього графічного інтерфейсу додатку.
        Створює всі віджети (рамки, мітки, поля вводу, кнопки, таблицю, текстове поле статусу).
        """
        frm = tk.Frame(self.root)
        frm.pack(fill="both", expand=True)

        # Search
        searchfrm = tk.Frame(frm)
        searchfrm.pack(fill="x")
        tk.Label(searchfrm, text="Пошук:").pack(side="left")
        self.search_var = tk.StringVar()
        search_entry = tk.Entry(searchfrm, textvariable=self.search_var)
        search_entry.pack(side="left", fill="x", expand=True)
        self.search_var.trace_add('write', lambda *args: self.apply_filter())

        # Folder list
        top = tk.Frame(frm)
        top.pack(fill="x")
        self.lst = tk.Listbox(top, height=4)
        self.lst.pack(side="left", fill="x", expand=True)
        btns = tk.Frame(top)
        btns.pack(side="right")
        tk.Button(btns, text="Додати", command=self.add_folder).pack(fill="x")
        tk.Button(btns, text="Видалити", command=self.remove_folder).pack(fill="x")
        tk.Button(btns, text="Очистити", command=self.clear_folders).pack(fill="x")

        # Event filter
        evfrm = tk.LabelFrame(frm, text="Фільтр подій")
        evfrm.pack(fill="x")
        self.ev_vars = {}
        for ev in ['created','modified','deleted','moved']:
            var = tk.BooleanVar(value=(ev in self.event_filter))
            self.ev_vars[ev] = var
            tk.Checkbutton(evfrm, text=ev, variable=var).pack(side="left")

        # Telegram
        tgfrm = tk.LabelFrame(frm, text="Telegram")
        tgfrm.pack(fill="x")
        self.tg_enable = tk.BooleanVar(value=bool(self.notifier.enabled()))
        tk.Checkbutton(tgfrm, text="Надсилати події", variable=self.tg_enable).pack(anchor="w")
        self.tg_token = tk.Entry(tgfrm, show="*")
        self.tg_chat = tk.Entry(tgfrm, show="*")
        tk.Label(tgfrm, text="Token:").pack(anchor="w")
        self.tg_token.pack(fill="x")
        self.tg_token.insert(0,self.config.get('telegram',{}).get('token',''))
        tk.Label(tgfrm, text="Chat ID:").pack(anchor="w")
        self.tg_chat.pack(fill="x")
        self.tg_chat.insert(0,self.config.get('telegram',{}).get('chat_id',''))

        # Control buttons
        ctrl = tk.Frame(frm)
        ctrl.pack(fill="x")
        self.btn_start = tk.Button(ctrl, text="▶ Запустити", command=self.start_monitoring)
        self.btn_stop = tk.Button(ctrl, text="⏹ Зупинити", command=self.stop_monitoring, state="disabled")
        self.btn_clear = tk.Button(ctrl, text="🧹 Очистити таблицю", command=self.clear_table)
        self.btn_export = tk.Button(ctrl, text="💾 Експорт CSV", command=self.export_csv)
        self.btn_start.pack(side="left")
        self.btn_stop.pack(side="left")
        self.btn_clear.pack(side="left")
        self.btn_export.pack(side="right")

        # Event table
        self.tree = ttk.Treeview(frm, columns=("ts","event","path","dest"), show="headings")
        for col, txt in [("ts","Час"),("event","Подія"),("path","Шлях"),("dest","Куди")]:
            self.tree.heading(col, text=txt, command=lambda c=col: self.sort_tree(c, False))
        self.tree.pack(fill="both", expand=True)

        # Status box
        self.status = tk.Text(frm, height=5)
        self.status.pack(fill="x")

        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Vasyl Zozulia")
        self.status_bar = tk.Label(
            self.root,
            textvariable=self.status_var,
            bd=1,
            relief=tk.SUNKEN,
            anchor="w"
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def add_folder(self):
    	"""
        Відкриває діалог для вибору каталогу та додає обраний шлях до списку для моніторингу.
        """
        folder = filedialog.askdirectory()
        if folder and folder not in self.paths:
            self.paths.append(folder)
            self.lst.insert("end", folder)

    def remove_folder(self):
    	"""
        Видаляє вибрані каталоги зі списку моніторингу.
        """
        sel = list(self.lst.curselection())
        for i in reversed(sel):
            path = self.lst.get(i)
            self.paths.remove(path)
            self.lst.delete(i)

    def clear_folders(self):
    	"""
    	Очищає весь список каталогів для моніторингу.
    	"""
        self.paths.clear()
        self.lst.delete(0,"end")

    def start_monitoring(self):
    	"""
        Запускає моніторинг файлової системи в окремому потоці.
        """
        if self.thread and self.thread.is_alive():
            messagebox.showinfo("Увага", "Моніторинг вже запущено")
            return
        if not self.paths:
            messagebox.showwarning("Немає", "Додайте каталог")
            return
        evs = {ev for ev,var in self.ev_vars.items() if var.get()}
        self.thread = WatcherThread(self.paths, evs, self.on_event, self.append_status)
        self.thread.start()
        self.btn_start.config(state="disabled")
        self.btn_stop.config(state="normal")

    def stop_monitoring(self):
    	"""
        Зупиняє моніторинг, викликаючи метод `stop` у потоці моніторингу.
        """
        if self.thread:
            self.thread.stop()
            self.thread = None
        self.btn_start.config(state="normal")
        self.btn_stop.config(state="disabled")

    def on_event(self, ts, evtype, path, dest):
    	"""
        Колбек-функція, яка викликається потоком моніторингу при виявленні події.
       	"""
        self._all_events.append((ts, evtype, path, dest))
        self.apply_filter()
        if self.tg_enable.get():
            self.notifier.token = self.tg_token.get()
            self.notifier.chat_id = self.tg_chat.get()
            text = f"[{ts}] {evtype.upper()}\n{path}" + (f"\n→ {dest}" if dest else "")
            self.notifier.send_async(text)

    def apply_filter(self):
    	"""
        Фільтрує та оновлює вміст таблиці `Treeview` на основі тексту в полі пошуку.
        """
        search_text = self.search_var.get().lower()
        for iid in self.tree.get_children():
            self.tree.delete(iid)
        count = 0
        for ts, evtype, path, dest in self._all_events:
            row = (ts, evtype, path, dest)
            if search_text and not any(search_text in str(x).lower() for x in row):
                continue
            iid = self.tree.insert("", "end", values=row)
            color = MyHandler.COLOR_MAP.get(evtype, "black")
            self.tree.item(iid, tags=(color,))
            self.tree.tag_configure(color, foreground=color)
            count += 1
            if count >= TREE_MAX_ROWS:
                break

    def clear_table(self):
    	"""
        Очищає як внутрішній список подій, так і візуальну таблицю `Treeview`.
        """
        self._all_events.clear()
        for iid in self.tree.get_children():
            self.tree.delete(iid)

    def sort_tree(self, col, reverse):
    	"""
        Сортує дані в таблиці `Treeview` за вибраним стовпцем.
        """
        data = [(self.tree.set(k, col), k) for k in self.tree.get_children("")]
        try:
            data.sort(key=lambda t: datetime.strptime(t[0], "%Y-%m-%d %H:%M:%S"), reverse=reverse)
        except:
            data.sort(reverse=reverse)
        for index, (val, k) in enumerate(data):
            self.tree.move(k, '', index)
        self.tree.heading(col, command=lambda: self.sort_tree(col, not reverse))

    
    def append_status(self, msg):
    	"""
        Додає повідомлення до текстового поля статусу.
        """
        self.root.after(0, lambda: self.status.insert("end", msg+"\n"))

    
    def export_csv(self):
    	"""
        Експортує всі події з внутрішнього списку до CSV-файлу.
        """
        path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV","*.csv")])
        if not path:
            return
        try:
            with open(path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(["timestamp","event_type","path","dest_path"])
                for ts, evtype, path, dest in self._all_events:
                    writer.writerow([ts, evtype, path, dest])
            messagebox.showinfo("OK", f"CSV збережено у {path}")
        except Exception as e:
            messagebox.showerror("Помилка", str(e))

    def on_close(self):
    	"""
        Метод, який викликається при закритті вікна додатку.
        """
        if self.thread:
            self.thread.stop()
            self.thread = None
        db_buffer.flush()
        save_folders(self.paths)
        save_config(self)
        self.root.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    app = FileMonitorApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()
