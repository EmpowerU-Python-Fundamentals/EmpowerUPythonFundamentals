import os
import sys
import tkinter as tk
from tkinter import ttk
from keylooker import key_looker as key
from keylooker import module as m
from network_tester import tester as t




class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.root = self
        self.log_file_name = "app_log.log"
        self.log_pass = m.get_log_file_path(self.log_file_name)
        self.title("Main window")
        self.geometry("400x200")
        background_lable = tk.Label(self.root, bg="grey")
        background_lable.place(x=0, y=0, relwidth=1, relheight=1)
        self.network_tester_window = None
        self.button = ttk.Button(self, text="Keylooker", command=lambda: self.on_button_click("Keylooker"))
        self.button.pack(pady=10)
        
        self.button2 = ttk.Button(self, text="Network tester", command=lambda: self.on_button_click("Network Tester"))
        self.button2.pack(pady=10)
        
        style = ttk.Style(self)
        style.configure("Custom.TLabel", background="grey", foreground="black", font=('Arial',12))
        

        self.label = ttk.Label(self, text="Choose an option", style="Custom.TLabel")
        self.label.pack(pady=40)
        # -----------------------------------------------

    def on_button_click(self, button_name):

        if button_name == "Keylooker":
            self.label.config(text=f"{button_name} Started")
            self.log_message(f"{button_name} Started")
            key.run_key_looker()
        else:
            self.label.config(text=f"{button_name} Started")
            self.log_message(f"{button_name} Started")
            # t.Apl()
            self.network_tester_window = t.Apl() 
            self.network_tester_window.update_idletasks()
            self.network_tester_window.update()
            # Переводим окно Network Tester на передний план (если оно уже открыто)
            self.network_tester_window.lift() 
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
            print(f"Error writing to log file {self.log_pass}: {e}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
