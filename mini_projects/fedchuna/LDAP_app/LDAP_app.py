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




    
class LD(tk.Toplevel):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.root = self
        self.log_file_name = "ldap.log"
        self.log_pass = m.get_log_file_path(self.log_file_name)
        self.log_message("---Aplication Inicialized---")
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
        
        
    def get_resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.dirname(os.path.abspath(__file__))

        return os.path.join(base_path, relative_path)

    def log_message(self,message):
        
        """ Writes a timestamped message to the specified log file. """
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