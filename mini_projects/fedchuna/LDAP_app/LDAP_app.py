from keylooker import module as m
from . import modules_ldap as m_l
from . import athorization as auth_windows
import os
import sys
from tkinter.scrolledtext import ScrolledText
import tkinter as tk
from tkinter import ttk

# Добавляем родительскую директорию в путь для импорта модулей
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)



class LD(tk.Toplevel):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.root = self
        self.log_file_name = "ldap.log"
        self.log_pass = m.get_log_file_path(self.log_file_name)
        self.config_file_name = "ldap_config.cfg"
        self.ldap_conf_pass = get_config_file_path(self.config_file_name)
        
        self.ldap_server = ''
        self.bind_dn = '' 
        self.bind_password = ''
        self.base_dn = ''
        self.filter = ''
        self.filter_for_group = ''
        self.ldap_connection = None 
        self.is_connected = False 

        self.ldap_conf_lines = ldap_conf_lines(self.ldap_conf_pass)
        self.log_message("---Application Initialized---")

        self.title("Ldap Module")
        self.geometry("600x550")
        self.resizable(False, False)
        self.config(bg="grey")
        
        style = ttk.Style(self)
        style.configure("Custom.TLabel", background="grey", foreground="black", font=('Arial',12))
        
        self.main_frame = ttk.Frame(self, style="Custom.TLabel", relief="flat", borderwidth=0)
        self.main_frame.pack(expand=True, padx=20, pady=20)
        
        self.output_text = ScrolledText(self.main_frame, wrap=tk.WORD, height=10, width=50, font=('Arial', 10))
        self.output_text.tag_configure("h1", font=("Arial", 11, "bold"))
        self.output_text.grid(row=6, column=0, columnspan=2, pady=10, sticky="nsew") 
        self.main_frame.grid_rowconfigure(5, weight=1) 
        self.main_frame.grid_columnconfigure(0, weight=1) 

        self.connect_disconnect_button = tk.Button(self, 
                                                   text="Connect LDAP", 
                                                   command=self.toggle_ldap_connection,
                                                   font=('Arial', 10), width=15, relief="raised")
        self.connect_disconnect_button.pack(pady=5)
        
        self.get_oath_data()
        
        config_buttons_frame = ttk.Frame(self, style="Custom.TLabel", relief="flat", borderwidth=0)
        config_buttons_frame.pack(pady=10)

        if self.ldap_conf_lines != 6:
            btn = tk.Button(config_buttons_frame, text="Создать конфиг", command=lambda: self.open_config_window(is_change=False))
            btn.pack(side=tk.LEFT, padx=5)
        else:
            btn2 = tk.Button(config_buttons_frame, text="Изменить конфиг", command=lambda: self.open_config_window(is_change=True))
            btn2.pack(side=tk.LEFT, padx=5)
        
        current_row = 0 
        
        self.label = ttk.Label(self.main_frame, text="Введите имя пользователя для поиска", style="Custom.TLabel")
        self.label.grid(row=current_row, column=0, columnspan=2, pady=(15, 5), sticky="n")
        current_row += 1
        
        self.entry = ttk.Entry(self.main_frame)
        self.entry.grid(row=current_row, column=0, columnspan=2, pady=5, sticky="ew")
        self.entry.bind("<Return>", lambda event: self.on_button_click("Search"))
        current_row += 1
        
        self.button = tk.Button(self.main_frame, text="Поиск", command=lambda: self.on_button_click("Search"),
                                 font=('Arial', 10), width=10, relief="raised")
        self.button.grid(row=current_row, column=0, columnspan=2, pady=5, sticky="n")
        current_row += 1
        self.main_frame.grid_columnconfigure(0, weight=1) 
        
        self.label1 = ttk.Label(self.main_frame, text="Введите имя группы для поиска", style="Custom.TLabel")
        self.label1.grid(row=current_row, column=0, columnspan=2, pady=(15, 5), sticky="n")
        current_row += 1
        
        self.entry1 = ttk.Entry(self.main_frame)
        self.entry1.grid(row=current_row, column=0, columnspan=2, pady=5, sticky="ew")
        self.entry1.bind("<Return>", lambda event: self.on_button_click("Search_group"))
        current_row += 1
        
        self.button1 = tk.Button(self.main_frame, text="Поиск", command=lambda: self.on_button_click("Search_group"),
                                 font=('Arial', 10), width=10, relief="raised")
        self.button1.grid(row=current_row, column=0, columnspan=2, pady=5, sticky="n")
        current_row += 1
        self.main_frame.grid_columnconfigure(0, weight=1) 
        
    def _extract_cn(self, dn_string: str) -> str:
        """Извлекает значение CN из строки DN."""
        try:
            cn_part = dn_string.split(',')[0]
            if cn_part.upper().startswith('CN='):
                return cn_part[3:]
        except Exception:
            pass
        return dn_string

    def _decode_ldap_value(self, value: any) -> str:
        if isinstance(value, bytes):
            return value.decode('utf-8', 'replace')
        return str(value) if value is not None else ''

    def get_oath_data(self):
        """Загружает данные конфигурации LDAP из файла."""
        try:
            with open(self.ldap_conf_pass, 'r', encoding='utf-8') as conf_f:
                lines = conf_f.readlines()
                if len(lines) == 6:
                    self.ldap_server = lines[0].replace('LDAP server: ', '').strip()
                    self.bind_dn = lines[1].replace('Bind DN: ', '').strip()
                    self.bind_password = lines[2].replace('Bind Password: ', '').strip()
                    self.base_dn = lines[3].replace('Base DN: ', '').strip()
                    self.filter = lines[4].replace('Filter: ', '').strip()
                    self.filter_for_group = lines[5].replace('Filter for Group: ', '').strip()
                    
                    print("LDAP Configuration Loaded:")
                    print(f"  LDAP Server: {self.ldap_server}")
                    print(f"  Bind DN: {self.bind_dn}")
                    print(f"  Bind Password: {'*' * len(self.bind_password)}") 
                    print(f"  Base DN: {self.base_dn}")
                    print(f"  Filter: {self.filter}")
                    print(f"  Filter for Group: {self.filter_for_group}")
                    self.log_message("LDAP configuration loaded successfully.")
                    self.update_connect_button_state() 
                    return True
                else:
                    print("Файл конфигурации содержит менее 5 строк. Данные неполные.")
                    self.log_message("Configuration file incomplete.")
                    self.update_connect_button_state() 
                    return False
        except FileNotFoundError:
            print(f"Файл конфигурации {self.ldap_conf_pass} не найден.")
            self.log_message(f"Configuration file {self.ldap_conf_pass} not found.")
            self.update_connect_button_state() 
            return False
        except Exception as e:
            print(f"Ошибка загрузки конфигурации: {e}")
            self.log_message(f"Error loading configuration: {e}")
            self.update_connect_button_state() 
            return False
        
    def open_config_window(self, is_change=False):
        """Открывает окно конфигурации LDAP."""
        auth_windows.LDAPAuthConfigWindow(
            master=self,
            pas=self.ldap_conf_pass,
            change_config=is_change
        )
        # После закрытия окна обновляем данные и состояние кнопок
        self.get_oath_data()
        self.update_connect_button_state()

    def update_connect_button_state(self):
        """Обновляет состояние кнопки Connect/Disconnect на основе загруженной конфигурации."""
        if self.ldap_server and self.bind_dn and self.bind_password and self.base_dn and self.filter:
            self.connect_disconnect_button.config(state=tk.NORMAL) 
        else:
            self.connect_disconnect_button.config(state=tk.DISABLED) 
            self.output_text.insert(tk.END, "Конфигурация LDAP неполная. Пожалуйста, настройте ее.\n")
            self.log_message("LDAP configuration incomplete.")

    def toggle_ldap_connection(self):
        """Переключает состояние LDAP-соединения."""
        self.output_text.delete(1.0, tk.END) 

        if not self.is_connected:
            self.output_text.insert(tk.END, "Попытка подключения к LDAP...\n")
            self.log_message("Attempting to connect to LDAP.")
            try:
                self.output_text.insert(tk.END, f"Сервер: {self.ldap_server}\n")
                self.output_text.insert(tk.END, f"Bind DN: {self.bind_dn}\n")
                self.ldap_connection = m_l.bind(self.ldap_server, self.bind_dn, self.bind_password) 
                
                if self.ldap_connection: 
                    self.is_connected = True
                    self.connect_disconnect_button.config(text="Disconnect LDAP")
                    self.output_text.insert(tk.END, "LDAP-соединение успешно установлено! ✅\n")
                    self.log_message("LDAP connection successful.")
                else:
                    self.output_text.insert(tk.END, "Ошибка подключения к LDAP. Проверьте учетные данные/сервер. ❌\n")
                    self.log_message("LDAP connection failed.")
                    
            except Exception as e:
                self.output_text.insert(tk.END, f"Ошибка подключения к LDAP: {e} ❌\n")
                self.log_message(f"Error connecting to LDAP: {e}")
                
        else:
            self.output_text.insert(tk.END, "Попытка отключения от LDAP...\n")
            self.log_message("Attempting to disconnect from LDAP.")
            try:
                if self.ldap_connection:
                    m_l.close_bind(self.ldap_connection) 
                
                self.is_connected = False
                self.ldap_connection = None 
                self.connect_disconnect_button.config(text="Connect LDAP")
                self.output_text.insert(tk.END, "LDAP-соединение успешно разорвано! 🔌\n")
                self.log_message("LDAP disconnected successfully.")
            except Exception as e:
                self.output_text.insert(tk.END, f"Ошибка при отключении от LDAP: {e}\n")
                self.log_message(f"Error disconnecting from LDAP: {e}")
                
        self.output_text.see(tk.END)

    def on_button_click(self, button_name):
        if button_name == "Search":
            self.label.config(text=f"Выполняется поиск пользователя...")
            self.log_message(f"{button_name} Started")
            self.on_search_click() 
            self.label.config(text="Введите имя пользователя для поиска")
            self.log_message(f"{button_name} had closed")
        elif button_name == "Search_group":
            self.label1.config(text=f"Выполняется поиск группы...")
            self.log_message(f"{button_name} Started")
            self.on_search_group_click()    
            self.label1.config(text="Введите имя группы для поиска")
            self.log_message(f"{button_name} had closed")

    def on_search_click(self):
        raw_username = self.entry.get().strip() 
        self.output_text.delete(1.0, tk.END) 

        if not raw_username:
            self.output_text.insert(tk.END, "Пожалуйста, введите имя пользователя.\n")
            self.log_message("Имя пользователя не предоставлено.")
            return
        
        if not self.is_connected:
            self.output_text.insert(tk.END, "Нет подключения к LDAP. Пожалуйста, подключитесь сначала.\n")
            self.log_message("Попытка поиска не удалась: не подключено к LDAP.")
            return

        search_by_attribute = "sAMAccountName" 
        if self.filter:
            first_attribute = self.filter.split(',')[0].strip()
            if first_attribute:
                search_by_attribute = first_attribute
        
        search_filter_string = f"(&(objectClass=user)({search_by_attribute}=*{raw_username}*))"

        search_attributes_list = [attr.strip() for attr in self.filter.split(',')] if self.filter else []
        if not search_attributes_list:
            search_attributes_list = ['distinguishedName', 'cn', 'mail', 'sAMAccountName', 'description', 'telephoneNumber', 'memberOf']
            
        self.output_text.insert(tk.END, f"Начинаем поиск для '{raw_username}'...\n\n") 
        self.log_message(f"Searching for '{raw_username}' by attribute '{search_by_attribute}' with filter: '{search_filter_string}'")
        
        try:
            search_result = m_l.search(
                self.ldap_connection, 
                self.base_dn, 
                search_filter_string, 
                search_attributes_list
            ) 
            
            if search_result:
                self.output_text.insert(tk.END, "Поиск успешно завершен. Найдены следующие результаты:\n\n")
                for dn, entry in search_result:
                    decoded_dn = self._decode_ldap_value(dn)
                    user_cn = self._extract_cn(decoded_dn)

                    self.output_text.insert(tk.END, f"Пользователь: {user_cn}\n", "h1")
                    
                    for attr_bytes in sorted(entry.keys()):
                        attr = self._decode_ldap_value(attr_bytes)
                        values = entry[attr_bytes]
                        if not values:
                            continue

                        if attr.lower() == 'memberof':
                            self.output_text.insert(tk.END, "  Входит в группы:\n")
                            for member_dn_bytes in values:
                                member_dn = self._decode_ldap_value(member_dn_bytes)
                                self.output_text.insert(tk.END, f"    - {self._extract_cn(member_dn)}\n")
                        else:
                            for value_bytes in values:
                                self.output_text.insert(tk.END, f"  {attr}: {self._decode_ldap_value(value_bytes)}\n")
                    self.output_text.insert(tk.END, "--------------------------------------------------\n\n")
                self.output_text.insert(tk.END, "\nВсе результаты поиска отображены.\n")
            else:
                self.output_text.insert(tk.END, f"Поиск завершен. Пользователь '{raw_username}' не найден.\n")
            self.log_message(f"Search for {raw_username} completed.")
        except Exception as e:
            self.output_text.insert(tk.END, f"!!! КРИТИЧЕСКАЯ ОШИБКА ПРИ ПОИСКЕ !!!\n")
            self.output_text.insert(tk.END, f"Тип ошибки: {type(e)}\n")
            self.output_text.insert(tk.END, f"Сообщение об ошибке: {e}\n")
            self.log_message(f"Критическая ошибка при поиске для {raw_username}: {e}")
        
        self.entry.delete(0, tk.END)
        self.output_text.see(tk.END)

    def on_search_group_click(self):
        raw_group_name = self.entry1.get().strip() 
        self.output_text.delete(1.0, tk.END)
        if not raw_group_name:
            self.output_text.insert(tk.END, "Пожалуйста, введите имя группы.\n")
            self.log_message("Имя группы не предоставлено.")
            return
        if not self.is_connected:
            self.output_text.insert(tk.END, "Нет подключения к LDAP. Пожалуйста, подключитесь сначала.\n")
            self.log_message("Попытка поиска группы не удалась: не подключено к LDAP.")
            return
        search_by_attribute = "cn"
        search_filter_string = f"(&(objectClass=group)({search_by_attribute}=*{raw_group_name}*))"
        search_attributes_list = [attr.strip() for attr in self.filter_for_group.split(',')] if self.filter_for_group else []
        if not search_attributes_list:
            search_attributes_list = ['cn', 'description', 'member']
        self.output_text.insert(tk.END, f"Начинаем поиск группы '{raw_group_name}'...\n\n")
        self.log_message(f"Searching for group '{raw_group_name}' by attribute '{search_by_attribute}' with filter: '{search_filter_string}'")
        try:
            search_result = m_l.search(
                self.ldap_connection, 
                self.base_dn, 
                search_filter_string, 
                search_attributes_list
            )
            if search_result:
                self.output_text.insert(tk.END, "Поиск успешно завершен. Найдены следующие результаты:\n\n")
                for dn, entry in search_result:
                    decoded_dn = self._decode_ldap_value(dn)
                    group_cn = self._extract_cn(decoded_dn)
                    
                    self.output_text.insert(tk.END, f"Группа: {group_cn}\n", "h1")
                    
                    for attr_bytes in sorted(entry.keys()):
                        attr = self._decode_ldap_value(attr_bytes)
                        values = entry[attr_bytes]
                        if not values:
                            continue
                        
                        if attr.lower() == 'member':
                            self.output_text.insert(tk.END, "  Участники:\n")
                            for member_dn_bytes in values:
                                member_dn = self._decode_ldap_value(member_dn_bytes)
                                self.output_text.insert(tk.END, f"    - {self._extract_cn(member_dn)}\n")
                        else:
                            for value_bytes in values:
                                self.output_text.insert(tk.END, f"  {attr}: {self._decode_ldap_value(value_bytes)}\n")
                    
                    self.output_text.insert(tk.END, "--------------------------------------------------\n\n")
                self.output_text.insert(tk.END, "\nВсе результаты поиска групп отображены.\n")
            else:
                self.output_text.insert(tk.END, f"Поиск завершен. Группа '{raw_group_name}' не найдена.\n")
            self.log_message(f"Search for group {raw_group_name} completed.")
        except Exception as e:
            self.output_text.insert(tk.END, f"!!! КРИТИЧЕСКАЯ ОШИБКА ПРИ ПОИСКЕ ГРУППЫ !!!\n")
            self.output_text.insert(tk.END, f"Тип ошибки: {type(e)}\n")
            self.output_text.insert(tk.END, f"Сообщение об ошибке: {e}\n")
            self.log_message(f"Критическая ошибка при поиске группы для {raw_group_name}: {e}")
        self.output_text.see(tk.END)
        self.entry1.delete(0, tk.END)


    def log_message(self,message):
        """Записывает сообщение с меткой времени в лог-файл."""
        try:
            with open(self.log_pass, 'a', encoding='utf-8') as log_f:
                log_f.write(f"{m.date_time()}:{message}\n")
        except Exception as e:
            print(f"Error writing to log file: {e}")

def get_config_file_path(cfg_file_name):
    """Определяет путь к файлу конфигурации."""
    cfg_directory_name = "config"
    if getattr(sys, 'frozen', False):
        base_dir = os.path.dirname(sys.executable) 
    else:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    cfg_dir_path = os.path.join(base_dir, cfg_directory_name)
    if not os.path.exists(cfg_dir_path):
        os.makedirs(cfg_dir_path)
        
    return os.path.join(cfg_dir_path, cfg_file_name)

def ldap_conf_lines(cfg_file):
    """Подсчитывает количество строк в файле конфигурации."""
    try:
        with open(cfg_file, 'r', encoding='utf-8') as cfg_f:
            return sum(1 for _ in cfg_f)
    except FileNotFoundError:
        return 0 
    except Exception as e: 
        print(f"Ошибка подсчета строк в файле конфигурации: {e}")
        return 0 

def run_standalone_tester():
    """Функция для автономного тестирования окна."""
    root_for_standalone = tk.Tk()
    root_for_standalone.withdraw() 
    app_tester = LD(root_for_standalone) 
    app_tester.protocol("WM_DELETE_WINDOW", lambda: on_standalone_close(app_tester, root_for_standalone))
    root_for_standalone.mainloop() 

def on_standalone_close(toplevel_window, root_window):
    """Обработчик закрытия для автономного теста."""
    toplevel_window.destroy()
    root_window.destroy()

if __name__ == "__main__":
    run_standalone_tester()
