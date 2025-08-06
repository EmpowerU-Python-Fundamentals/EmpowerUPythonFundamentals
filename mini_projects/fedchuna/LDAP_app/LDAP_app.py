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
# from . import modules_ldap as m_l
import modules_ldap as m_l
import athorization as Oath

    
class LD(tk.Toplevel):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.root = self
        self.log_file_name = "ldap.log"
        self.log_pass = m.get_log_file_path(self.log_file_name)
        self.config_file_name = "ldap_config.cfg"
        self.ldap_conf_pass = get_config_file_path(self.config_file_name)
        self.ldap_conf_lines = ldap_conf_lines(self.ldap_conf_pass)
        log_message("---Aplication Inicialized---")
        if self.ldap_conf_lines == 4:
            ldap_athorization() 
            """to write logic and authorization.py"""
        
        self.title("Ldap Module")
        self.geometry("600x550")
        self.resizable(False, False)
        self.config(bg="grey")
        
        style = ttk.Style(self)
        style.configure("Custom.TLabel", background="grey", foreground="black", font=('Arial',12))
        
        main_frame = ttk.Frame(self, style="Custom.TLabel", relief="flat", borderwidth=0)
        main_frame.pack(expand=True, padx=20, pady=20)
        current_row = 0
        
        
        
        self.label = ttk.Label(main_frame, text="Type Username to search", style="Custom.TLabel")
        self.label.grid(row=current_row, column=0, columnspan=2, pady=(15, 5), sticky="n")
        current_row += 1
        
        self.entry = ttk.Entry(main_frame)
        self.entry.grid(row=current_row, column=0, columnspan=2, pady=5, sticky="ew")
        self.entry.bind("<Return>", lambda event: self.on_button_click("Search"))  # Добавляем обработчик нажатия Enter
        current_row += 1
        
        self.button = tk.Button(main_frame, text="Search", command=lambda: self.on_button_click("Search"),
                                font=('Arial', 10), width=10, relief="raised") # Добавим шрифт, ширину и рельеф
        self.button.grid(row=current_row, column=0, columnspan=2, pady=5, sticky="n")
        current_row += 1
        main_frame.grid_columnconfigure(0, weight=1)
        
        self.output_text = ScrolledText(main_frame, wrap=tk.WORD, height=10, width=50, font=('Arial', 10))
        self.output_text.grid(row=current_row, column=0, columnspan=2, pady=10, sticky="nsew")
        current_row += 1 
        main_frame.grid_rowconfigure(current_row-1, weight=1)
    
    def on_button_click(self, button_name):
        
        if button_name == "Search":
            self.label.config(text=f"{button_name} Started")
            self.log_message(f"{button_name} Started")
            self.on_search_click()
        # else:
        #     self.label1.config(text=f"{button_name} Started")
        #     self.log_message(f"{button_name} Started")
        #     self.on_trace_click()
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
            with open(self.ldap_conf_pass, 'a', encoding='utf-8') as conf_f:
                conf_f.write(message)
        except Exception as e:
            print(f"Error writing to conf file: {e}")

    def on_search_click(self):
        username = self.entry.get().strip() 
        self.output_text.delete(1.0, tk.END) 

        if not username:
            self.output_text.insert(tk.END, "Please enter username.\n")
            self.log_message("Username not provided.")
            return

        self.output_text.insert(tk.END, f"Searchung {username}...\n")
        self.log_message(f"Searching {username}")
        search_result = m_l.search_user_test(username)

    

        try:
            process = subprocess.Popen(command, 
                                     stdout=subprocess.PIPE, 
                                     stderr=subprocess.PIPE, 
                                     universal_newlines=True, 
                                     encoding=target_encoding, 
                                     errors='replace') 
            stdout, stderr = process.communicate(timeout=10)

            if stdout:
                self.output_text.insert(tk.END, stdout)
                self.log_message(f"Ping {ip} successful:\n{stdout}")
            if stderr:
                self.output_text.insert(tk.END, f"Error:\n{stderr}")
                self.log_message(f"Ping {ip} error:\n{stderr}")

            if process.returncode == 0:
                self.output_text.insert(tk.END, f"\nPing to {ip} successful.\n")
            else:
                self.output_text.insert(tk.END, f"\nPing to {ip} failed with code {process.returncode}.\n")

        except subprocess.TimeoutExpired:
            process.kill()
            stdout, stderr = process.communicate()
            try:
                stdout_str = stdout.decode(target_encoding, errors='replace')
                stderr_str = stderr.decode(target_encoding, errors='replace')
            except Exception: 
                stdout_str = str(stdout) 
                stderr_str = str(stderr)

            self.output_text.insert(tk.END, f"Ping to {ip} timed out.\nOutput (if any):\n{stdout_str}\nErrors (if any):\n{stderr_str}\n")
            self.log_message(f"Ping to {ip} timed out.")
        except FileNotFoundError:
            self.output_text.insert(tk.END, "Ping command not found. Make sure it's in your system's PATH.\n")
            self.log_message("Ping command not found.")
        except Exception as e:
            self.output_text.insert(tk.END, f"An unexpected error occurred: {e}\n")
            self.log_message(f"Ping to {ip} unexpected error: {e}")
        
        self.output_text.see(tk.END)

def get_config_file_path(log_file_name):
    log_directory_name = "config"
    if getattr(sys, 'frozen', False):
        base_dir = os.path.dirname(sys.executable) 
    else:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    log_dir_path = os.path.join(base_dir, log_directory_name)
    if not os.path.exists(log_dir_path):
        os.makedirs(log_dir_path)
        
    return os.path.join(log_dir_path, log_file_name)    

def ldap_conf_lines(cfg_file):
    try:
        with open(cfg_file, 'r', encoding='utf-8') as cfg_f:
            line_count = int(0)
            for line in cfg_f:
                line_count += 1
            return line_count
    except FileNotFoundError as fe:
        log_message(fe)
        
def log_message(self,message):
    
    """ Writes a timestamped message to the specified config file. """
    try:
        with open(self.log_pass, 'a', encoding='utf-8') as log_f:
            log_f.write(f"{m.date_time()}:{message}\n")
    except Exception as e:
        print(f"Error writing to log file: {e}")

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