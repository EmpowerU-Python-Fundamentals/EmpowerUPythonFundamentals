import os
import sys
import subprocess
import platform
from tkinter.scrolledtext import ScrolledText
from pathlib import Path
import tkinter as tk
from tkinter import ttk 

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from keylooker import module as m
from . import modules_ldap as m_l 
from . import athorization as Oath 

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
        self.filter = '' # This will store the comma-separated string of attributes
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
        self.output_text.grid(row=5, column=0, columnspan=2, pady=10, sticky="nsew") 
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

        if self.ldap_conf_lines != 5: # Changed to 5 lines for filter
            btn = tk.Button(config_buttons_frame, text="Open Oath", command=lambda: self.open_oath_window(self.ldap_conf_pass))
            btn.pack(side=tk.LEFT, padx=5)
        else:
            btn2 = tk.Button(config_buttons_frame, text="Open OathChange", command=lambda: self.open_oathch_window(self.ldap_conf_pass))
            btn2.pack(side=tk.LEFT, padx=5)
        
        current_row = 0 
        
        self.label = ttk.Label(self.main_frame, text="Type Username to search", style="Custom.TLabel")
        self.label.grid(row=current_row, column=0, columnspan=2, pady=(15, 5), sticky="n")
        current_row += 1
        
        self.entry = ttk.Entry(self.main_frame)
        self.entry.grid(row=current_row, column=0, columnspan=2, pady=5, sticky="ew")
        self.entry.bind("<Return>", lambda event: self.on_button_click("Search"))
        current_row += 1
        
        self.button = tk.Button(self.main_frame, text="Search", command=lambda: self.on_button_click("Search"),
                                 font=('Arial', 10), width=10, relief="raised")
        self.button.grid(row=current_row, column=0, columnspan=2, pady=5, sticky="n")
        current_row += 1
        self.label.grid(row=0, column=0, columnspan=2, pady=(15, 5), sticky="n")
        self.entry.grid(row=1, column=0, columnspan=2, pady=5, sticky="ew")
        self.button.grid(row=2, column=0, columnspan=2, pady=5, sticky="n")
        self.main_frame.grid_columnconfigure(0, weight=1) 
    
    def get_oath_data(self):
        """Loads LDAP configuration data from file."""
        try:
            with open(self.ldap_conf_pass, 'r', encoding='utf-8') as conf_f:
                lines = conf_f.readlines()
                # Expect 5 lines now: server, bind_dn, bind_password, base_dn, filter
                if len(lines) == 5:
                    self.ldap_server = lines[0].replace('LDAP server: ', '').strip()
                    self.bind_dn = lines[1].replace('Bind DN: ', '').strip()
                    self.bind_password = lines[2].replace('Bind Password: ', '').strip()
                    self.base_dn = lines[3].replace('Base DN: ', '').strip()
                    self.filter = lines[4].replace('Filter: ', '').strip() # Load the filter string
                    
                    print(f"LDAP Configuration Loaded:")
                    print(f"LDAP Server: {self.ldap_server}")
                    print(f"Bind DN: {self.bind_dn}")
                    print(f"Bind Password: {'*' * len(self.bind_password)}") 
                    print(f"Base DN: {self.base_dn}")
                    print(f"Filter: {self.filter}") # Print the loaded filter
                    self.log_message("LDAP configuration loaded successfully.")
                    self.update_connect_button_state() 
                    # Return all 5 values
                    return self.ldap_server, self.bind_dn, self.bind_password, self.base_dn, self.filter
                else:
                    print("Configuration file has fewer than 5 lines. Incomplete data.")
                    self.log_message("Configuration file incomplete.")
                    self.update_connect_button_state() 
                    return False
        except FileNotFoundError:
            print(f"Configuration file {self.ldap_conf_pass} not found. Will prompt for new config.")
            self.log_message(f"Configuration file {self.ldap_conf_pass} not found.")
            self.update_connect_button_state() 
            return False
        except Exception as e:
            print(f"Error loading configuration: {e}")
            self.log_message(f"Error loading configuration: {e}")
            self.update_connect_button_state() 
            return False
        
    def open_oath_window(self, pas):
        Oath.LDAuth(master=self, pas=pas) 
        self.get_oath_data()
        self.update_connect_button_state() 
        
    def open_oathch_window(self, pas):
        Oath.LDAuthCh(master=self, pas=pas)
        self.get_oath_data()
        self.update_connect_button_state() 

    def update_connect_button_state(self):
        """Updates the state of the Connect/Disconnect button based on loaded config."""
        # Check if all 5 config values are present
        if self.ldap_server and self.bind_dn and self.bind_password and self.base_dn and self.filter:
            self.connect_disconnect_button.config(state=tk.NORMAL) 
        else:
            self.connect_disconnect_button.config(state=tk.DISABLED) 
            self.output_text.insert(tk.END, "LDAP configuration incomplete. Please set up via 'Open Oath'/'Open OathChange'.\n")
            self.log_message("LDAP configuration incomplete.")

    def toggle_ldap_connection(self):
        """Toggles the LDAP connection state."""
        self.output_text.delete(1.0, tk.END) 

        if not self.is_connected:
            self.output_text.insert(tk.END, "Attempting to connect to LDAP...\n")
            self.log_message("Attempting to connect to LDAP.")
            try:
                print(f"Connecting to LDAP server: {self.ldap_server}")
                self.output_text.insert(tk.END, f"Connecting to LDAP server: {self.ldap_server}\n")
                print(f"Bind DN: {self.bind_dn}")
                self.output_text.insert(tk.END, f"Bind DN: {self.bind_dn}\n")
                print(f"Bind Password: {'*' * len(self.bind_password)}") 
                self.output_text.insert(tk.END, f"Bind Password: {'*' * len(self.bind_password)}\n") 
                print(f"Base DN: {self.base_dn}")
                self.output_text.insert(tk.END, f"Base DN: {self.base_dn}\n")
                self.ldap_connection = m_l.bind(self.ldap_server, self.bind_dn, self.bind_password) 
                
                print(f"DEBUG: Type of self.ldap_connection after m_l.bind: {type(self.ldap_connection)}")

                if self.ldap_connection: 
                    self.is_connected = True
                    self.connect_disconnect_button.config(text="Disconnect LDAP", command=self.toggle_ldap_connection)
                    self.output_text.insert(tk.END, "LDAP connection successful! ✅\n")
                    self.log_message("LDAP connection successful.")
                else:
                    self.output_text.insert(tk.END, "LDAP connection failed. Check credentials/server. ❌\n")
                    self.log_message("LDAP connection failed.")
                    
            except Exception as e:
                self.output_text.insert(tk.END, f"Error connecting to LDAP: {e} ❌\n")
                self.log_message(f"Error connecting to LDAP: {e}")
                
        else:
            self.output_text.insert(tk.END, "Attempting to disconnect from LDAP...\n")
            self.log_message("Attempting to disconnect from LDAP.")
            try:
                if self.ldap_connection:
                    m_l.close_bind(self.ldap_connection) 
                
                self.is_connected = False
                self.ldap_connection = None 
                self.connect_disconnect_button.config(text="Connect LDAP", command=self.toggle_ldap_connection)
                self.output_text.insert(tk.END, "LDAP disconnected successfully! 🔌\n")
                self.log_message("LDAP disconnected successfully.")
            except Exception as e:
                self.output_text.insert(tk.END, f"Error disconnecting from LDAP: {e}\n")
                self.log_message(f"Error disconnecting from LDAP: {e}")
                
        self.output_text.see(tk.END)

    def on_button_click(self, button_name):
        if button_name == "Search":
            self.label.config(text=f"{button_name} Started")
            self.log_message(f"{button_name} Started")
            self.on_search_click() 
            self.log_message(f"{button_name} had closed")

    def get_resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(base_path, relative_path)

    def config_messagge(self,message):
        """ Writes config to the specified config file. """
        try:
            # Changed 'a' to 'w' to overwrite the file when saving config,
            # ensuring only the latest config is present.
            with open(self.ldap_conf_pass, 'w', encoding='utf-8') as conf_f:
                conf_f.write(message) 
        except Exception as e:
            print(f"Error writing to conf file: {e}")

    def on_search_click(self):
        # Get the raw username from the entry field
        raw_username = self.entry.get().strip() 
        self.output_text.delete(1.0, tk.END) 

        if not raw_username:
            self.output_text.insert(tk.END, "Пожалуйста, введите имя пользователя.\n") # Updated message
            self.log_message("Имя пользователя не предоставлено.")
            return
        
        if not self.is_connected:
            self.output_text.insert(tk.END, "Не подключено к LDAP. Пожалуйста, подключитесь сначала.\n") # Updated message
            self.log_message("Попытка поиска не удалась: не подключено к LDAP.")
            return

        # Determine the attribute to search by based on the first item in self.filter
        # If self.filter is empty or malformed, default to 'sAMAccountName'
        search_by_attribute = "sAMAccountName" 
        if self.filter:
            # Split the filter string by comma, strip whitespace, and take the first element
            first_attribute = self.filter.split(',')[0].strip()
            if first_attribute:
                search_by_attribute = first_attribute
        
        search_filter_string = f"(&(objectClass=user)({search_by_attribute}=*{raw_username}*))"

        # Parse the self.filter string (e.g., "cn, mail, sAMAccountName") into a list of attributes
        search_attributes_list = [attr.strip() for attr in self.filter.split(',')] if self.filter else []
        if not search_attributes_list:
            # Fallback to a default set of attributes if the filter string is empty or invalid
            search_attributes_list = ['distinguishedName', 'cn', 'mail', 'sAMAccountName', 'description', 'telephoneNumber']
        self.output_text.insert(tk.END, f"Начинаем поиск для '{raw_username}' по атрибуту '{search_by_attribute}' с фильтром: '{search_filter_string}'...\n") 
        self.log_message(f"Начинаем поиск для '{raw_username}' по атрибуту '{search_by_attribute}' с фильтром: '{search_filter_string}'")
        
        try:
            search_result = m_l.search_user_test(
                self.ldap_connection, 
                self.base_dn, 
                search_filter_string, 
                search_attributes_list
            ) 
            
            if search_result:
                self.output_text.insert(tk.END, "Поиск успешно завершен. Найдены следующие результаты:\n") # Updated message
                for dn, entry in search_result:
                    # Safely decode DN:
                    decoded_dn = dn
                    if isinstance(dn, bytes):
                        try:
                            decoded_dn = dn.decode('utf-8')
                        except UnicodeDecodeError:
                            decoded_dn = str(dn) # Fallback if decoding fails
                    
                    self.output_text.insert(tk.END, f"  Найден: {decoded_dn}\n") 
                    for attr, value in entry.items():
                        # Ensure value is a list/iterable before accessing [0] and decode safely
                        # Check if value[0] is bytes before decoding
                        if isinstance(value, list) and len(value) > 0:
                            if isinstance(value[0], bytes):
                                try:
                                    decoded_value = value[0].decode('utf-8')
                                except UnicodeDecodeError:
                                    decoded_value = str(value[0]) # Fallback if decoding fails
                            else:
                                decoded_value = str(value[0]) # Already a string or other type
                            self.output_text.insert(tk.END, f"    {attr}: {decoded_value}\n")
                        else:
                            self.output_text.insert(tk.END, f"    {attr}: {value}\n") # Handle non-list values
                self.output_text.insert(tk.END, "\nВсе результаты поиска отображены.\n") # Updated message
            else:
                self.output_text.insert(tk.END, f"Поиск завершен. Пользователь '{raw_username}' не найден по атрибуту '{search_by_attribute}'.\n") # Updated message
            self.log_message(f"Search for {raw_username} completed.")

        except Exception as e:
            self.output_text.insert(tk.END, f"!!! КРИТИЧЕСКАЯ ОШИБКА ПРИ ПОИСКЕ !!!\n")
            self.output_text.insert(tk.END, f"Тип ошибки: {type(e)}\n")
            self.output_text.insert(tk.END, f"Сообщение об ошибке: {e}\n")
            self.log_message(f"Критическая ошибка при поиске для {raw_username}: {e}")
        
        self.output_text.see(tk.END)

    def log_message(self,message):
        """ Writes a timestamped message to the specified log file. """
        try:
            with open(self.log_pass, 'a', encoding='utf-8') as log_f:
                log_f.write(f"{m.date_time()}:{message}\n")
        except Exception as e:
            print(f"Error writing to log file: {e}")

def get_config_file_path(cfg_file_name):
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
    try:
        with open(cfg_file, 'r', encoding='utf-8') as cfg_f:
            line_count = 0
            for _ in cfg_f: 
                line_count += 1
            return line_count
    except FileNotFoundError:
        return 0 
    except Exception as e: 
        print(f"Error counting lines in config file: {e}")
        return 0 

def run_standalone_tester():
    root_for_standalone = tk.Tk()
    root_for_standalone.withdraw() 

    app_tester = LD(root_for_standalone) 
    
    app_tester.protocol("WM_DELETE_WINDOW", lambda: on_standalone_close(app_tester, root_for_standalone))
    
    root_for_standalone.mainloop() 

def on_standalone_close(toplevel_window, root_window):
    toplevel_window.destroy()
    root_window.destroy()

if __name__ == "__main__":
    run_standalone_tester()
