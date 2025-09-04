import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from generator import generate_password
from validator import validate_input
import pyperclip
import datetime
import os
import random
from accountant_data import ACCOUNTANT_PASSWORDS

def copy_password():
    """Копіює згенерований пароль у буфер обміну."""
    password = password_display.cget("text").split('\n')[0]
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Успішно", "Пароль скопійовано!")
    else:
        messagebox.showwarning("Помилка", "Немає пароля для копіювання.")

def save_password():
    """Зберігає згенерований пароль у файл."""
    resource = resource_entry.get()
    password = password_display.cget("text").split('\n')[0]
    date_created = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    if not password:
        messagebox.showwarning("Помилка", "Немає пароля для збереження.")
        return

    try:
        with open("passwords.txt", "a", encoding="utf-8") as f:
            f.write(f"Ресурс: {resource if resource else 'Без назви'} | Пароль: {password} | Дата: {date_created}\n")
        messagebox.showinfo("Успішно", "Пароль збережено у файл passwords.txt")
        # Очищаємо поля після успішного збереження
        resource_entry.delete(0, tk.END)
        password_display.config(text="")
        refresh_passwords()
    except Exception as e:
        messagebox.showerror("Помилка збереження", f"Не вдалося зберегти файл: {e}")

def generate_and_display():
    """
    Функція-обробник для кнопки "Згенерувати".
    Зчитує параметри з полів введення, перевіряє їх і генерує пароль.
    """
    length = length_entry.get()
    use_letters = letters_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()
    use_uppercase = uppercase_var.get()
    exclude_ambiguous = ambiguous_var.get()
    is_accountant_mode = accountant_var.get()

    if is_accountant_mode:
        password = random.choice(ACCOUNTANT_PASSWORDS)
        password_display.config(text=password)
    else:
        is_valid, error_message = validate_input(length, use_letters, use_numbers, use_symbols, use_uppercase)
        
        if not is_valid:
            messagebox.showerror("Помилка вводу", error_message)
            return
            
        generated_password = generate_password(
            length=int(length),
            use_letters=use_letters,
            use_numbers=use_numbers,
            use_symbols=use_symbols,
            use_uppercase=use_uppercase,
            exclude_ambiguous=exclude_ambiguous,
            is_accountant_mode=is_accountant_mode
        )
        
        password_display.config(text=generated_password)

def refresh_passwords():
    """Оновлює таблицю збережених паролів, читаючи дані з файлу."""
    for item in tree.get_children():
        tree.delete(item)
    
    try:
        if os.path.exists("passwords.txt"):
            with open("passwords.txt", "r", encoding="utf-8") as f:
                for i, line in enumerate(f):
                    parts = line.strip().split(" | ")
                    if len(parts) == 3:
                        resource = parts[0].replace("Ресурс: ", "")
                        password = parts[1].replace("Пароль: ", "")
                        date = parts[2].replace("Дата: ", "")
                        tree.insert("", tk.END, iid=i, values=("☐", resource, password, date))
        
    except FileNotFoundError:
        messagebox.showinfo("Повідомлення", "Файл passwords.txt ще не існує.")

def copy_from_tree(event):
    """Копіює пароль з виділеного рядка таблиці у буфер обміну."""
    selected_item = tree.focus()
    if selected_item:
        password = tree.item(selected_item, 'values')[2]
        pyperclip.copy(password)
        messagebox.showinfo("Успішно", "Пароль скопійовано!")
    else:
        messagebox.showwarning("Помилка", "Будь ласка, виберіть рядок для копіювання.")

def edit_password(event):
    """Дозволяє редагувати пароль подвійним кліком."""
    item_id = tree.identify_row(event.y)
    col = tree.identify_column(event.x)
    
    if col == '#3':
        x, y, w, h = tree.bbox(item_id, column=col)
        
        edit_entry = ttk.Entry(tree)
        edit_entry.place(x=x, y=y, width=w, height=h)
        edit_entry.insert(0, tree.item(item_id, 'values')[2])
        edit_entry.focus()
        
        def save_edit(e):
            new_password = edit_entry.get()
            
            with open("passwords.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()
            
            resource = tree.item(item_id, 'values')[1]
            date = tree.item(item_id, 'values')[3]
            
            lines[int(item_id)] = f"Ресурс: {resource} | Пароль: {new_password} | Дата: {date}\n"
            
            with open("passwords.txt", "w", encoding="utf-8") as f:
                f.writelines(lines)

            edit_entry.destroy()
            refresh_passwords()
            
        edit_entry.bind('<Return>', save_edit)
        edit_entry.bind('<FocusOut>', lambda e: edit_entry.destroy())

def toggle_checkbox(event):
    """Перемикає стан чекбокса при кліку на відповідну комірку."""
    item = tree.identify_row(event.y)
    col = tree.identify_column(event.x)
    
    if col == '#1':
        values = list(tree.item(item, 'values'))
        
        if values[0] == "☐":
            values[0] = "✅"
        else:
            values[0] = "☐"
        
        tree.item(item, values=values)
    
def delete_selected_passwords():
    """Видаляє вибрані паролі з файлу та оновлює таблицю."""
    selected_items = [item for item in tree.get_children() if tree.item(item, 'values')[0] == "✅"]
    if not selected_items:
        messagebox.showwarning("Помилка", "Будь ласка, виберіть паролі для видалення.")
        return
    
    if messagebox.askyesno("Підтвердження", f"Ви впевнені, що хочете видалити {len(selected_items)} паролів?"):
        try:
            with open("passwords.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()
            
            lines_to_delete = {int(item) for item in selected_items}
            lines_to_keep = [line for i, line in enumerate(lines) if i not in lines_to_delete]
            
            with open("passwords.txt", "w", encoding="utf-8") as f:
                f.writelines(lines_to_keep)
                
            messagebox.showinfo("Успішно", "Вибрані паролі видалено!")
            refresh_passwords()
        except Exception as e:
            messagebox.showerror("Помилка", f"Не вдалося видалити паролі: {e}")

def toggle_accountant_mode():
    """Вимикає/вмикає інші чекбокси в залежності від стану 'Я бухгалтер'."""
    state = accountant_var.get()
    if state:
        letters_checkbox.config(state=tk.DISABLED)
        uppercase_checkbox.config(state=tk.DISABLED)
        numbers_checkbox.config(state=tk.DISABLED)
        symbols_checkbox.config(state=tk.DISABLED)
        ambiguous_checkbox.config(state=tk.DISABLED)
        length_entry.config(state=tk.DISABLED)
        length_entry.delete(0, tk.END)
        length_entry.insert(0, "8")
        password_display.config(text="")
    else:
        letters_checkbox.config(state=tk.NORMAL)
        uppercase_checkbox.config(state=tk.NORMAL)
        numbers_checkbox.config(state=tk.NORMAL)
        symbols_checkbox.config(state=tk.NORMAL)
        ambiguous_checkbox.config(state=tk.NORMAL)
        length_entry.config(state=tk.NORMAL)
        length_entry.delete(0, tk.END)
        length_entry.insert(0, "12")
        password_display.config(text="")


if __name__ == "__main__":
    # Створення головного вікна
    root = tk.Tk()
    root.title("Генератор паролів")
    root.geometry("450x575")
    root.resizable(False, False)

    # Примусове оновлення вікна для коректного рендерингу
    root.update()

    # Створення віджету з вкладками (Notebook)
    notebook = ttk.Notebook(root)
    notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Створення вкладок
    generator_tab = ttk.Frame(notebook)
    passwords_tab = ttk.Frame(notebook)

    notebook.add(generator_tab, text="Генератор")
    notebook.add(passwords_tab, text="Збережені паролі")

    # Вміст вкладки "Генератор"
    generator_frame = tk.Frame(generator_tab, padx=20, pady=20)
    generator_frame.pack(fill=tk.BOTH, expand=True)

    # Поле для введення ресурсу
    tk.Label(generator_frame, text="Ресурс (назва сайту/програми):").pack(anchor="w", pady=(0, 5))
    resource_entry = tk.Entry(generator_frame, width=30)
    resource_entry.pack(fill=tk.X, pady=(0, 15))

    # Поле для введення довжини
    tk.Label(generator_frame, text="Довжина пароля:").pack(anchor="w", pady=(0, 5))
    length_entry = tk.Entry(generator_frame, width=30)
    length_entry.insert(0, "12")
    length_entry.pack(fill=tk.X, pady=(0, 15))

    # Чекбокси для параметрів
    tk.Label(generator_frame, text="Включити:").pack(anchor="w", pady=(0, 5))
    
    letters_var = tk.BooleanVar(value=True)
    letters_checkbox = tk.Checkbutton(generator_frame, text="Літери (a-z)", variable=letters_var)
    letters_checkbox.pack(anchor="w")

    uppercase_var = tk.BooleanVar(value=True)
    uppercase_checkbox = tk.Checkbutton(generator_frame, text="Великі літери (A-Z)", variable=uppercase_var)
    uppercase_checkbox.pack(anchor="w")
    
    numbers_var = tk.BooleanVar(value=True)
    numbers_checkbox = tk.Checkbutton(generator_frame, text="Цифри (0-9)", variable=numbers_var)
    numbers_checkbox.pack(anchor="w")
    
    symbols_var = tk.BooleanVar(value=True)
    symbols_checkbox = tk.Checkbutton(generator_frame, text="Символи (!@#)", variable=symbols_var)
    symbols_checkbox.pack(anchor="w")

    ambiguous_var = tk.BooleanVar(value=False)
    ambiguous_checkbox = tk.Checkbutton(generator_frame, text="Виключити неоднозначні символи", variable=ambiguous_var)
    ambiguous_checkbox.pack(anchor="w", pady=(5, 10))

    # Новий чекбокс для режиму бухгалтера
    accountant_var = tk.BooleanVar(value=False)
    accountant_checkbox = tk.Checkbutton(generator_frame, text="Я бухгалтер", variable=accountant_var, command=toggle_accountant_mode)
    accountant_checkbox.pack(anchor="w", pady=(5, 10))

    # Кнопка для генерації
    generate_button = tk.Button(generator_frame, text="Згенерувати пароль", command=generate_and_display)
    generate_button.pack(fill=tk.X, pady=10)
    
    # Поле для виведення результату
    tk.Label(generator_frame, text="Згенерований пароль:").pack(anchor="w", pady=(0, 5))
    password_display = tk.Label(generator_frame, text="", bg="lightgray", padx=10, pady=10, relief="solid", wraplength=400, justify="left")
    password_display.pack(fill=tk.X)

    # Кнопки для копіювання та збереження
    button_frame = tk.Frame(generator_frame)
    button_frame.pack(fill=tk.X, pady=10)
    
    copy_button = tk.Button(button_frame, text="Копіювати", command=copy_password)
    copy_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))
    
    save_button = tk.Button(button_frame, text="Зберегти", command=save_password)
    save_button.pack(side=tk.RIGHT, expand=True, fill=tk.X, padx=(5, 0))

    # Вміст вкладки "Збережені паролі"
    passwords_frame = tk.Frame(passwords_tab, padx=20, pady=20)
    passwords_frame.pack(fill=tk.BOTH, expand=True)

    # Створення таблиці (Treeview)
    tree = ttk.Treeview(passwords_frame, columns=("Чекбокс", "Ресурс", "Пароль", "Дата"), show="headings")
    tree.heading("Чекбокс", text="✓", anchor=tk.CENTER)
    tree.heading("Ресурс", text="Ресурс")
    tree.heading("Пароль", text="Пароль")
    tree.heading("Дата", text="Дата")

    tree.column("Чекбокс", width=30, anchor=tk.CENTER)
    tree.column("Ресурс", width=120)
    tree.column("Пароль", width=150)
    tree.column("Дата", width=120)
    
    # Додаємо скролбари
    scrollbar_v = ttk.Scrollbar(passwords_frame, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscrollcommand=scrollbar_v.set)
    scrollbar_v.pack(side=tk.RIGHT, fill=tk.Y)
    
    tree.pack(fill=tk.BOTH, expand=True)
    
    # Додаємо фрейм для кнопок та скролбару
    controls_frame = tk.Frame(passwords_frame)
    controls_frame.pack(fill=tk.X, pady=(10, 0))

    scrollbar_h = ttk.Scrollbar(passwords_frame, orient=tk.HORIZONTAL, command=tree.xview)
    tree.configure(xscrollcommand=scrollbar_h.set)
    scrollbar_h.pack(side=tk.TOP, fill=tk.X, before=controls_frame)

    # Фрейм для центрування кнопок
    button_center_frame = tk.Frame(controls_frame)
    button_center_frame.pack(anchor=tk.CENTER)
    
    # Кнопки для оновлення та видалення
    refresh_button = tk.Button(button_center_frame, text="Оновити", command=refresh_passwords)
    refresh_button.pack(side=tk.LEFT, padx=(0, 5))
    
    delete_button = tk.Button(button_center_frame, text="Видалити", command=delete_selected_passwords)
    delete_button.pack(side=tk.LEFT, padx=(5, 0))

    # Додаємо можливість копіювання за допомогою правої кнопки миші та редагування подвійним кліком
    tree.bind("<Button-3>", copy_from_tree)
    tree.bind("<Double-1>", edit_password)
    
    # Прив'язуємо обробник події тільки до першої колонки
    tree.bind("<Button-1>", toggle_checkbox)
    
    # Завантажуємо паролі при першому запуску вкладки
    refresh_passwords()

    root.mainloop()