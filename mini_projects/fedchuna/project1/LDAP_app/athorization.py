import os
import sys
from tkinter.scrolledtext import ScrolledText
import tkinter as tk
from tkinter import ttk

 
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from keylooker import module as m

class LDAPAuthConfigWindow(tk.Toplevel):


    def __init__(self, master=None, pas=None, change_config=False):
        super().__init__(master)
        self.ldap_conf_pass = pas

        if change_config:
            self.title("Изменение конфигурации LDAP")
            self._delete_config_file()
        else:
            self.title("Новая конфигурация LDAP")


        self.config_data = {
            'ldap_server': 'ldap://',
            'bind_dn': '',
            'bind_password': '',
            'base_dn': '',
            'filter': '',
            'filter_for_group': ''
        }

        self.geometry("350x400")
        self.resizable(False, False)
        self.config(bg="grey")

        style = ttk.Style(self)
        style.configure("Custom.TLabel", background="grey", foreground="black", font=('Arial', 10))

        self.main_frame = ttk.Frame(self, style="Custom.TLabel", relief="flat", borderwidth=0)
        self.main_frame.pack(expand=True, padx=10, pady=10)


        self.widgets = {}
        self._create_widgets()

        self.output_text = ScrolledText(self.main_frame, wrap=tk.WORD, height=5, width=40, font=('Arial', 9))
        self.output_text.grid(row=3, column=0, columnspan=2, pady=5, sticky="nsew")
        self.main_frame.grid_rowconfigure(3, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        self._show_step("Ldap_server")


        self.grab_set()
        self.focus_set()
        self.transient(master)
        self.wait_window()

    def _create_widgets(self):
        """Создает и хранит все виджеты для шагов мастера."""
        steps_info = {
            "Ldap_server": ("Введите LDAP Server", self._confirm_server),
            "LDAP_DN": ("Введите Bind DN", self._confirm_dn),
            "Password": ("Введите пароль для Bind", self._confirm_password),
            "Base_DN": ("Введите Base DN для поиска", self._confirm_base_dn),
            "Filter": ("Введите атрибуты (через запятую)", self._confirm_filter),
            "Filter_for_group": ("Введите атрибуты для групп (через запятую)", self._confirm_filter_for_group)
        }

        for name, (text, command) in steps_info.items():
            label = ttk.Label(self.main_frame, text=text, style="Custom.TLabel")
            entry = ttk.Entry(self.main_frame, show="*" if name == "Password" else "")
            button = tk.Button(self.main_frame, text="Confirm", command=command,
                               font=('Arial', 9), width=8, relief="raised")
            entry.bind("<Return>", lambda event, cmd=command: cmd())
            self.widgets[name] = (label, entry, button)

    def _show_step(self, name):
        """Отображает виджеты для указанного шага."""
        label, entry, button = self.widgets[name]
        label.grid(row=0, column=0, columnspan=2, pady=(5, 2), sticky="n")
        entry.grid(row=1, column=0, columnspan=2, pady=2, sticky="ew")
        button.grid(row=2, column=0, columnspan=2, pady=2, sticky="n")
        entry.focus_set()

    def _hide_step(self, name):
        """Скрывает виджеты для указанного шага."""
        for widget in self.widgets[name]:
            widget.grid_forget()

    def _confirm_server(self):
        value = self.widgets["Ldap_server"][1].get().strip()
        if not value:
            self.output_text.insert(tk.END, "LDAP server не может быть пустым.\n")
        else:
            self.config_data['ldap_server'] = 'ldap://' + value
            self.output_text.insert(tk.END, f"LDAP server установлен: {self.config_data['ldap_server']}\n")
            self._hide_step("Ldap_server")
            self._show_step("LDAP_DN")

    def _confirm_dn(self):
        value = self.widgets["LDAP_DN"][1].get().strip()
        if not value:
            self.output_text.insert(tk.END, "Bind DN не может быть пустым.\n")
        else:
            self.config_data['bind_dn'] = value
            self.output_text.insert(tk.END, "Bind DN установлен.\n")
            self._hide_step("LDAP_DN")
            self._show_step("Password")

    def _confirm_password(self):
        value = self.widgets["Password"][1].get().strip()
        if not value:
            self.output_text.insert(tk.END, "Пароль не может быть пустым.\n")
        else:
            self.config_data['bind_password'] = value
            self.output_text.insert(tk.END, "Пароль установлен.\n")
            self._hide_step("Password")
            self._show_step("Base_DN")

    def _confirm_base_dn(self):
        value = self.widgets["Base_DN"][1].get().strip()
        if not value:
            self.output_text.insert(tk.END, "Base DN не может быть пустым.\n")
        else:
            self.config_data['base_dn'] = value
            self.output_text.insert(tk.END, "Base DN установлен.\n")
            self._hide_step("Base_DN")
            self._show_step("Filter")

    def _confirm_filter(self):
        value = self.widgets["Filter"][1].get().strip()
        if not value:
            self.output_text.insert(tk.END, "Атрибуты фильтра не могут быть пустыми.\n")
        else:
            self.config_data['filter'] = value
            self.output_text.insert(tk.END, f"Фильтр установлен: {self.config_data['filter']}\n")
            self._hide_step("Filter")
            self._show_step("Filter_for_group")
    
    def _confirm_filter_for_group(self):
        value = self.widgets["Filter_for_group"][1].get().strip()
        if not value:
            self.output_text.insert(tk.END, "Атрибуты фильтра для групп не могут быть пустыми.\n")
        else:
            self.config_data['filter_for_group'] = value
            self.output_text.insert(tk.END, f"Фильтр для групп установлен: {self.config_data['filter_for_group']}\n")
            self._hide_step("Filter_for_group")
            self._finish_and_save()


    def _finish_and_save(self):
        """Отображает итоговую информацию, сохраняет конфигурацию и закрывает окно."""
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, "Конфигурация завершена!\n\n")
        self.output_text.insert(tk.END, f"LDAP Server: {self.config_data['ldap_server']}\n")
        self.output_text.insert(tk.END, f"Bind DN: {self.config_data['bind_dn']}\n")
        self.output_text.insert(tk.END, f"Bind Password: {'*' * len(self.config_data['bind_password'])}\n")
        self.output_text.insert(tk.END, f"Base DN: {self.config_data['base_dn']}\n")
        self.output_text.insert(tk.END, f"Filter: {self.config_data['filter']}\n")
        self.output_text.insert(tk.END, f"Filter for Group: {self.config_data['filter_for_group']}\n")
        
        self._save_config_to_file()

        done_button = tk.Button(self.main_frame, text="Done", command=self.destroy,
                                font=('Arial', 9), width=8, relief="raised")
        done_button.grid(row=4, column=0, columnspan=2, pady=10)
        self.output_text.grid(row=0, column=0, columnspan=2, pady=5, sticky="nsew", rowspan=4)

    def _save_config_to_file(self):
        """Записывает всю собранную конфигурацию в файл, перезаписывая его."""
        try:
            config_content = (
                f"LDAP server: {self.config_data['ldap_server']}\n"
                f"Bind DN: {self.config_data['bind_dn']}\n"
                f"Bind Password: {self.config_data['bind_password']}\n"
                f"Base DN: {self.config_data['base_dn']}\n"
                f"Filter: {self.config_data['filter']}\n"
                f"Filter for Group: {self.config_data['filter_for_group']}\n"
            )
            with open(self.ldap_conf_pass, 'w', encoding='utf-8') as conf_f:
                conf_f.write(config_content)
            self.output_text.insert(tk.END, "\nКонфигурация успешно сохранена.\n")
        except Exception as e:
            print(f"Ошибка записи в файл конфигурации: {e}")
            self.output_text.insert(tk.END, f"\nОшибка сохранения конфигурации: {e}\n")

    def _delete_config_file(self):
        """Удаляет файл конфигурации, если он существует."""
        try:
            if os.path.exists(self.ldap_conf_pass):
                os.remove(self.ldap_conf_pass)
                print(f"Файл '{self.ldap_conf_pass}' успешно удален.🗑️")
        except FileNotFoundError:
            pass
        except PermissionError:
            print(f"Ошибка: Недостаточно прав для удаления файла '{self.ldap_conf_pass}'.")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка при удалении файла: {e}")

def run_standalone_tester():
    """Функция для автономного тестирования окна конфигурации."""
    root_for_standalone = tk.Tk()
    root_for_standalone.withdraw()
    app_tester = LDAPAuthConfigWindow(root_for_standalone, pas="ldap_config.cfg")
    app_tester.protocol("WM_DELETE_WINDOW", lambda: on_standalone_close(app_tester, root_for_standalone))
    root_for_standalone.mainloop()

def on_standalone_close(toplevel_window, root_window):
    """Обработчик закрытия для автономного теста."""
    toplevel_window.destroy()
    root_window.destroy()

if __name__ == "__main__":
    run_standalone_tester()
