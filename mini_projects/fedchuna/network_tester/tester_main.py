import os
import sys
from pathlib import Path
import tkinter as tk
from tkinter import ttk


parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from keylooker import key_looker as key
from keylooker import module as m


class Apl(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.root = self
        self.log_file_name = "tester_log.log"
        self.log_pass = m.get_log_file_path(self.log_file_name)
        self.log_message("---Aplication Inicialized---")
        self.title("Main window")
        self.geometry("600x400")
        background_lable = tk.Label(self.root, bg="grey")
        background_lable.place(x=0, y=0, relwidth=1, relheight=1)
        
        style = ttk.Style(self)
        style.configure("Custom.TLabel", background="grey", foreground="black", font=('Arial',12))
        
        
        self.label = ttk.Label(self, text="Type IP address to check:", style="Custom.TLabel")
        self.label.pack(pady=30)
        self.entry = ttk.Entry(self)
        self.entry.pack()
        self.label1 = ttk.Label(self, text="Type IP address to trace:", style="Custom.TLabel")
        self.label1.pack(pady=30)
        self.entry2 = ttk.Entry(self)
        self.entry2.pack()        
        
        



    
    
    def on_button_click(self, button_name):

        if button_name == "Keylooker":
            self.label.config(text=f"{button_name} Started")
            self.log_message(f"{button_name} Started")
            key.run_key_looker()
        else:
            self.label.config(text=f"{button_name} Started")
            self.log_message(f"{button_name} Started")
        self.log_message(f"{button_name} had closed")
    
    def get_resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.dirname(os.path.abspath(__file__))

        return os.path.join(base_path, relative_path)

# --- Функція для логування, щоб уникнути дублювання коду ---
    def log_message(self,message):
        """ Writes a timestamped message to the specified log file. """
        try:
            with open(self.log_pass, 'a', encoding='utf-8') as log_f:
                log_f.write(f"{m.date_time()}:{message}\n")
        except Exception as e:
            print(f"Error writing to log file: {e}")
        
        
if __name__ == "__main__":
    app = Apl()
    app.mainloop()