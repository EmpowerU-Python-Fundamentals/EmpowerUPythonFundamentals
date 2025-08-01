import os
import sys
import tkinter as tk
from tkinter import ttk
from keylooker import key_looker as key # Импорт key_looker
from keylooker import module as m
from network_tester import tester as t # Предполагаем, что вы используете tester.py как основной


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
        self.keylooker_window = None # Добавляем переменную для окна Keylooker

        self.button = ttk.Button(self, text="Keylooker", command=lambda: self.on_button_click("Keylooker"))
        self.button.pack(pady=10)
        
        self.button2 = ttk.Button(self, text="Network tester", command=lambda: self.on_button_click("Network Tester"))
        self.button2.pack(pady=10)
        
        style = ttk.Style(self)
        style.configure("Custom.TLabel", background="grey", foreground="black", font=('Arial',12))
        
        self.label = ttk.Label(self, text="Choose an option", style="Custom.TLabel")
        self.label.pack(pady=40)

    def on_button_click(self, button_name):
        self.label.config(text=f"{button_name} Started")
        self.log_message(f"{button_name} Started")
        
        self.withdraw() # Скрываем главное окно App сразу, независимо от того, какая кнопка нажата

        if button_name == "Keylooker":
            # Проверяем, существует ли окно Keylooker и открыто ли оно
            if self.keylooker_window is None or not self.keylooker_window.winfo_exists():
              
                key.run_key_looker()
                self.deiconify() 

                self.log_message("Keylooker window started (manual parent restore may be needed if it's a blocking app).")

            else: 
                self.keylooker_window.lift()
        
        else:
            if self.network_tester_window is None or not self.network_tester_window.winfo_exists():
                self.network_tester_window = t.Apl(self.root) 
                self.network_tester_window.protocol("WM_DELETE_WINDOW", self.on_network_tester_close)
                
                self.network_tester_window.update_idletasks()
                self.network_tester_window.update()
            self.network_tester_window.lift() 
        self.log_message(f"{button_name} had closed (parent window hidden).")
    
    def on_network_tester_close(self):

        if self.network_tester_window is not None:
            self.network_tester_window.destroy()
            self.network_tester_window = None
        self.deiconify()
        self.log_message("Network Tester Closed. Main window restored.")


    def on_keylooker_close(self):

        if self.keylooker_window is not None:
            self.keylooker_window.destroy()
            self.keylooker_window = None 
        self.deiconify()
        self.log_message("Keylooker Closed. Main window restored.")

    def get_resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(base_path, relative_path)

    def log_message(self,message):
        
        try:
            with open(self.log_pass, 'a', encoding='utf-8') as log_f:
                log_f.write(f"{m.date_time()}:{message}\n")
        except Exception as e:
            print(f"Error writing to log file {self.log_pass}: {e}")


if __name__ == "__main__":
    app = App()
    app.mainloop()