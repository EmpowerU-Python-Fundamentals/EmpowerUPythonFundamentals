import os
import sys
from pathlib import Path
import tkinter as tk
from tkinter import ttk # Все равно нужен для ttk.Label и ttk.Entry


parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from keylooker import key_looker as key
from keylooker import module as m


class Apl(tk.Toplevel): 
    
    def __init__(self, master=None):
        super().__init__(master) 
        self.root = self
        self.log_file_name = "tester_log.log"
        self.log_pass = m.get_log_file_path(self.log_file_name)
        self.log_message("---Aplication Inicialized---")
        self.title("Main window")
        self.geometry("600x400") 
        self.resizable(False, False) 
        
        self.config(bg="grey") 
        
        style = ttk.Style(self)
        style.configure("Custom.TLabel", background="grey", foreground="black", font=('Arial',12))
      
        
        main_frame = ttk.Frame(self, style="Custom.TLabel", relief="flat", borderwidth=0) 
        main_frame.pack(expand=True, padx=20, pady=20) 

        current_row = 0

        self.label = ttk.Label(main_frame, text="Type IP address to check:", style="Custom.TLabel")
        self.label.grid(row=current_row, column=0, columnspan=2, pady=(15, 5), sticky="n") 
        current_row += 1
        
        self.entry = ttk.Entry(main_frame)
        self.entry.grid(row=current_row, column=0, columnspan=2, pady=5, sticky="ew") 
        current_row += 1
        
        
        self.button = tk.Button(main_frame, text="ping", command=lambda: self.on_button_click("Ping"),
                                font=('Arial', 10), width=10, relief="raised") # Добавим шрифт, ширину и рельеф
        self.button.grid(row=current_row, column=0, columnspan=2, pady=5, sticky="n") 
        current_row += 1
        
        self.label1 = ttk.Label(main_frame, text="Type IP address to trace:", style="Custom.TLabel")
        self.label1.grid(row=current_row, column=0, columnspan=2, pady=(20, 5), sticky="n")
        current_row += 1
        
        self.entry2 = ttk.Entry(main_frame)
        self.entry2.grid(row=current_row, column=0, columnspan=2, pady=5, sticky="ew")
        current_row += 1
        
       
        self.button2 = tk.Button(main_frame, text="trace", command=lambda: self.on_button_click("trace"),
                                 font=('Arial', 10), width=10, relief="raised") 
        self.button2.grid(row=current_row, column=0, columnspan=2, pady=5, sticky="n")
        current_row += 1

        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)


    def on_button_click(self, button_name):
        
        if button_name == "Ping":
            self.label.config(text=f"{button_name} Started")
            self.log_message(f"{button_name} Started")
            self.on_check_click()
        else:
            self.label1.config(text=f"{button_name} Started")
            self.log_message(f"{button_name} Started")
            self.on_trace_click()
        self.log_message(f"{button_name} had closed")
    
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
    
    
    def on_check_click(self):
        
        ip = self.entry.get()
        print(f"Checking IP: {ip}")


    def on_trace_click(self):
        
        ip = self.entry2.get()
        print(f"Tracing IP: {ip}")


def run_standalone_tester():
    
    root_for_standalone = tk.Tk()
    root_for_standalone.withdraw() 

    app_tester = Apl(root_for_standalone) 
    
    app_tester.protocol("WM_DELETE_WINDOW", lambda: on_standalone_close(app_tester, root_for_standalone))
    
    root_for_standalone.mainloop() 

def on_standalone_close(toplevel_window, root_window):

    toplevel_window.destroy()
    root_window.destroy()

if __name__ == "__main__":
    run_standalone_tester()