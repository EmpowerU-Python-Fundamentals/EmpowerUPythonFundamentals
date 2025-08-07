import os
import sys
from tkinter.scrolledtext import ScrolledText
import tkinter as tk
from tkinter import ttk 

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from keylooker import module as m
from . import modules_ldap as m_l 
from . import athorization as Oath 

class LDAuth(tk.Toplevel):
    
    def __init__(self, master=None, pas=None):
        super().__init__(master)
        self.root = self
        self.log_file_name = "ldap.log"
        self.log_pass = m.get_log_file_path(self.log_file_name)
        self.config_file_name = "ldap_config.cfg"
        self.ldap_conf_pass = pas
        print(pas)
        self.ldap_server = 'ldap://' 
        self.bind_dn = '' 
        self.bind_password = ''
        self.base_dn = ''
        self.filter = '' 
        self.title("LDAP OAUth")
        self.geometry("350x350") 
        self.resizable(False, False)
        self.config(bg="grey")
        
        style = ttk.Style(self)
        style.configure("Custom.TLabel", background="grey", foreground="black", font=('Arial',10)) 
        
        main_frame = ttk.Frame(self, style="Custom.TLabel", relief="flat", borderwidth=0)
        main_frame.pack(expand=True, padx=10, pady=10) 
        
        self.label = ttk.Label(main_frame, text="Type ldap_server", style="Custom.TLabel")
        self.entry = ttk.Entry(main_frame)
        self.button = tk.Button(main_frame, text="Confirm", command=lambda: self.on_button_click("Ldap_server_Confirm"),
                                 font=('Arial', 9), width=8, relief="raised")
        self.entry.bind("<Return>", lambda event: self.on_button_click("Ldap_server_Confirm"))

        self.label1 = ttk.Label(main_frame, text="Type ldap_DN", style="Custom.TLabel")
        self.entry1 = ttk.Entry(main_frame)
        self.button1 = tk.Button(main_frame, text="Confirm", command=lambda: self.on_button_click("LDAP_DN_Confirm"),
                                 font=('Arial', 9), width=8, relief="raised")
        self.entry1.bind("<Return>", lambda event: self.on_button_click("LDAP_DN_Confirm"))

        self.label2 = ttk.Label(main_frame, text="Type admin ldap password", style="Custom.TLabel")
        self.entry2 = ttk.Entry(main_frame, show="*") 
        self.button2 = tk.Button(main_frame, text="Confirm", command=lambda: self.on_button_click("Password_Confirm"),
                                 font=('Arial', 9), width=8, relief="raised")
        self.entry2.bind("<Return>", lambda event: self.on_button_click("Password_Confirm"))

        self.label3 = ttk.Label(main_frame, text="Type Ldap Base DN", style="Custom.TLabel") 
        self.entry3 = ttk.Entry(main_frame)
        self.button3 = tk.Button(main_frame, text="Confirm", command=lambda: self.on_button_click("Base_DN_Confirm"),
                                 font=('Arial', 9), width=8, relief="raised")
        self.entry3.bind("<Return>", lambda event: self.on_button_click("Base_DN_Confirm"))
        
        # Corrected label text for the filter input
        self.label4 = ttk.Label(main_frame, text="Type Ldap Filter", style="Custom.TLabel") 
        self.entry4 = ttk.Entry(main_frame)
        self.button4 = tk.Button(main_frame, text="Confirm", command=lambda: self.on_button_click("Filter_Confirm"),
                                 font=('Arial', 9), width=8, relief="raised")
        self.entry4.bind("<Return>", lambda event: self.on_button_click("Filter_Confirm"))
        
        self.output_text1 = ScrolledText(main_frame, wrap=tk.WORD, height=5, width=40, font=('Arial', 9))

        
        self.label.grid(row=0, column=0, columnspan=2, pady=(5, 2), sticky="n")
        self.entry.grid(row=1, column=0, columnspan=2, pady=2, sticky="ew")
        self.button.grid(row=2, column=0, columnspan=2, pady=2, sticky="n")
        
        
        self.output_text1.grid(row=3, column=0, columnspan=2, pady=5, sticky="nsew")
        main_frame.grid_rowconfigure(3, weight=1) 
        main_frame.grid_columnconfigure(0, weight=1)
        self.grab_set()
        self.focus_set()
        self.transient(master)
        self.wait_window()
    def config_messagge(self,message):
        
        """ Writes config to the specified config file. """
        try:
            with open(self.ldap_conf_pass, 'a', encoding='utf-8') as conf_f:
                conf_f.write(message)
        except Exception as e:
            print(f"Error writing to conf file: {e}")
        
    def on_button_click(self, button_type):
            
            
        self.output_text1.delete(1.0, tk.END) 
        self.oath_data = list()
        if button_type == "Ldap_server_Confirm":
            ldap_server_value = self.entry.get().strip()
            if not ldap_server_value:
                self.output_text1.insert(tk.END, "LDAP server wasn't entered\n")
            else:
                self.ldap_server = 'ldap://' + ldap_server_value
                self.config_messagge(f"LDAP server: {self.ldap_server}\n")
                self.output_text1.insert(tk.END, f"LDAP server set to: {self.ldap_server}\n")
                self.oath_data.append(f"ldap_server: {self.ldap_server}")

                
                self.label.grid_forget()
                self.entry.grid_forget()
                self.button.grid_forget()

                
                self.label1.grid(row=0, column=0, columnspan=2, pady=(5, 2), sticky="n")
                self.entry1.grid(row=1, column=0, columnspan=2, pady=2, sticky="ew")
                self.button1.grid(row=2, column=0, columnspan=2, pady=2, sticky="n")
                
                
                self.output_text1.grid(row=3, column=0, columnspan=2, pady=5, sticky="nsew")


        elif button_type == "LDAP_DN_Confirm":
            bind_dn_value = self.entry1.get().strip()
            if not bind_dn_value:
                self.output_text1.insert(tk.END, "CN DN wasn't entered\n")
            else:
                self.bind_dn = bind_dn_value
                self.config_messagge(f"Bind DN: {self.bind_dn}\n")
                self.output_text1.insert(tk.END, f"LDAP DN set to: {self.bind_dn}\n")
                self.oath_data.append(f"bind_dn: {self.bind_dn}")

                
                self.label1.grid_forget()
                self.entry1.grid_forget()
                self.button1.grid_forget()

                
                self.label2.grid(row=0, column=0, columnspan=2, pady=(5, 2), sticky="n")
                self.entry2.grid(row=1, column=0, columnspan=2, pady=2, sticky="ew")
                self.button2.grid(row=2, column=0, columnspan=2, pady=2, sticky="n")

                self.output_text1.grid(row=3, column=0, columnspan=2, pady=5, sticky="nsew")


        elif button_type == "Password_Confirm":
            bind_password_value = self.entry2.get().strip()
            if not bind_password_value:
                self.output_text1.insert(tk.END, "Your password is empty\n")
            else:
                self.bind_password = bind_password_value
                self.config_messagge(f"Bind Password: {self.bind_password}\n")
                self.output_text1.insert(tk.END, f"Password set\n")
                self.oath_data.append(f"bind_password: {self.bind_password}")

                
                self.label2.grid_forget()
                self.entry2.grid_forget()
                self.button2.grid_forget()

                
                self.label3.grid(row=0, column=0, columnspan=2, pady=(5, 2), sticky="n")
                self.entry3.grid(row=1, column=0, columnspan=2, pady=2, sticky="ew")
                self.button3.grid(row=2, column=0, columnspan=2, pady=2, sticky="n")

                self.output_text1.grid(row=3, column=0, columnspan=2, pady=5, sticky="nsew")


        elif button_type == "Base_DN_Confirm":
            base_dn_value = self.entry3.get().strip()
            if not base_dn_value:
                self.output_text1.insert(tk.END, "Base domain name and OU not entered\n")
            else:
                self.base_dn = base_dn_value
                self.config_messagge(f"Base DN: {self.base_dn}\n")
                self.output_text1.insert(tk.END, f"Base DN set to: {self.base_dn}\n")
                self.oath_data.append(f"base_dn: {self.base_dn}")

                
                self.label3.grid_forget()
                self.entry3.grid_forget()
                self.button3.grid_forget()
                
                # Show next set (Filter)
                self.label4.grid(row=0, column=0, columnspan=2, pady=(5, 2), sticky="n")
                self.entry4.grid(row=1, column=0, columnspan=2, pady=2, sticky="ew")
                self.button4.grid(row=2, column=0, columnspan=2, pady=2, sticky="n")

                self.output_text1.grid(row=3, column=0, columnspan=2, pady=5, sticky="nsew")


        elif button_type == "Filter_Confirm":
            filter_value = self.entry4.get().strip()
            if not filter_value:
                self.output_text1.insert(tk.END, "Filter not entered\n")
            else:
                self.filter = filter_value
                self.config_messagge(f"Filter: {self.filter}\n")
                self.output_text1.insert(tk.END, f"Filter set to: {self.filter}\n")
                self.oath_data.append(f"filter: {self.filter}")

                self.label4.grid_forget()
                self.entry4.grid_forget()
                self.button4.grid_forget()
                
                self.output_text1.insert(tk.END, "\nAll LDAP configuration data collected!\n")
                self.output_text1.insert(tk.END, f"LDAP Server: {self.ldap_server}\n")
                self.output_text1.insert(tk.END, f"Bind DN: {self.bind_dn}\n")
                self.output_text1.insert(tk.END, f"Bind Password: {'*' * len(self.bind_password)}\n") 
                self.output_text1.insert(tk.END, f"Base DN: {self.base_dn}\n")
                self.output_text1.insert(tk.END, f"Filter: {self.filter}\n")
                
                self.done_button = tk.Button(self.root, text="Done", command=self.destroy, 
                                                     font=('Arial', 9), width=8, relief="raised")
                self.done_button.pack(pady=10) 

                self.output_text1.grid(row=0, column=0, columnspan=2, pady=5, sticky="nsew") 

        self.output_text1.see(tk.END)
    
class LDAuthCh(tk.Toplevel):
    def __init__(self, master=None, pas=None):
        super().__init__(master)
        self.root = self
        self.log_file_name = "ldap.log"
        self.log_pass = m.get_log_file_path(self.log_file_name)
        self.config_file_name = "ldap_config.cfg"
        self.ldap_conf_pass = pas
        self.del_folder()
        print(pas)
        self.ldap_server = 'ldap://' 
        self.bind_dn = '' 
        self.bind_password = ''
        self.base_dn = ''
        self.filter = '' 
        self.title("LDAP OAUth")
        self.geometry("350x350") 
        self.resizable(False, False)
        self.config(bg="grey")
        
        style = ttk.Style(self)
        style.configure("Custom.TLabel", background="grey", foreground="black", font=('Arial',10)) 
        
        main_frame = ttk.Frame(self, style="Custom.TLabel", relief="flat", borderwidth=0)
        main_frame.pack(expand=True, padx=10, pady=10) 
        
        self.label = ttk.Label(main_frame, text="Type ldap_server", style="Custom.TLabel")
        self.entry = ttk.Entry(main_frame)
        self.button = tk.Button(main_frame, text="Confirm", command=lambda: self.on_button_click("Ldap_server_Confirm"),
                                 font=('Arial', 9), width=8, relief="raised")
        self.entry.bind("<Return>", lambda event: self.on_button_click("Ldap_server_Confirm"))

        self.label1 = ttk.Label(main_frame, text="Type ldap_DN", style="Custom.TLabel")
        self.entry1 = ttk.Entry(main_frame)
        self.button1 = tk.Button(main_frame, text="Confirm", command=lambda: self.on_button_click("LDAP_DN_Confirm"),
                                 font=('Arial', 9), width=8, relief="raised")
        self.entry1.bind("<Return>", lambda event: self.on_button_click("LDAP_DN_Confirm"))

        self.label2 = ttk.Label(main_frame, text="Type admin ldap password", style="Custom.TLabel")
        self.entry2 = ttk.Entry(main_frame, show="*") 
        self.button2 = tk.Button(main_frame, text="Confirm", command=lambda: self.on_button_click("Password_Confirm"),
                                 font=('Arial', 9), width=8, relief="raised")
        self.entry2.bind("<Return>", lambda event: self.on_button_click("Password_Confirm"))

        self.label3 = ttk.Label(main_frame, text="Type Ldap Base DN", style="Custom.TLabel") 
        self.entry3 = ttk.Entry(main_frame)
        self.button3 = tk.Button(main_frame, text="Confirm", command=lambda: self.on_button_click("Base_DN_Confirm"),
                                 font=('Arial', 9), width=8, relief="raised")
        self.entry3.bind("<Return>", lambda event: self.on_button_click("Base_DN_Confirm"))

        # Corrected label text for the filter input
        self.label4 = ttk.Label(main_frame, text="Type Ldap Filter", style="Custom.TLabel") 
        self.entry4 = ttk.Entry(main_frame)
        self.button4 = tk.Button(main_frame, text="Confirm", command=lambda: self.on_button_click("Filter_Confirm"),
                                 font=('Arial', 9), width=8, relief="raised")
        self.entry4.bind("<Return>", lambda event: self.on_button_click("Filter_Confirm"))
    
        self.output_text1 = ScrolledText(main_frame, wrap=tk.WORD, height=5, width=40, font=('Arial', 9))

        
        self.label.grid(row=0, column=0, columnspan=2, pady=(5, 2), sticky="n")
        self.entry.grid(row=1, column=0, columnspan=2, pady=2, sticky="ew")
        self.button.grid(row=2, column=0, columnspan=2, pady=2, sticky="n")
        
        
        self.output_text1.grid(row=3, column=0, columnspan=2, pady=5, sticky="nsew")
        main_frame.grid_rowconfigure(3, weight=1) 
        main_frame.grid_columnconfigure(0, weight=1)
        self.grab_set()
        self.focus_set()
        self.transient(master)
        self.wait_window()
    def config_messagge(self,message):
        
        """ Writes config to the specified config file. """
        try:
            with open(self.ldap_conf_pass, 'a', encoding='utf-8') as conf_f:
                conf_f.write(message)
        except Exception as e:
            print(f"Error writing to conf file: {e}")
        
    def on_button_click(self, button_type):
            
            
        self.output_text1.delete(1.0, tk.END) 
        self.oath_data = list()
        if button_type == "Ldap_server_Confirm":
            ldap_server_value = self.entry.get().strip()
            if not ldap_server_value:
                self.output_text1.insert(tk.END, "LDAP server wasn't entered\n")
            else:
                self.ldap_server = 'ldap://' + ldap_server_value
                self.config_messagge(f"LDAP server: {self.ldap_server}\n")
                self.output_text1.insert(tk.END, f"LDAP server set to: {self.ldap_server}\n")
                self.oath_data.append(f"ldap_server: {self.ldap_server}")

                
                self.label.grid_forget()
                self.entry.grid_forget()
                self.button.grid_forget()

                
                self.label1.grid(row=0, column=0, columnspan=2, pady=(5, 2), sticky="n")
                self.entry1.grid(row=1, column=0, columnspan=2, pady=2, sticky="ew")
                self.button1.grid(row=2, column=0, columnspan=2, pady=2, sticky="n")
                
                
                self.output_text1.grid(row=3, column=0, columnspan=2, pady=5, sticky="nsew")


        elif button_type == "LDAP_DN_Confirm":
            bind_dn_value = self.entry1.get().strip()
            if not bind_dn_value:
                self.output_text1.insert(tk.END, "CN DN wasn't entered\n")
            else:
                self.bind_dn = bind_dn_value
                self.config_messagge(f"Bind DN: {self.bind_dn}\n")
                self.output_text1.insert(tk.END, f"LDAP DN set to: {self.bind_dn}\n")
                self.oath_data.append(f"bind_dn: {self.bind_dn}")

                
                self.label1.grid_forget()
                self.entry1.grid_forget()
                self.button1.grid_forget()

                
                self.label2.grid(row=0, column=0, columnspan=2, pady=(5, 2), sticky="n")
                self.entry2.grid(row=1, column=0, columnspan=2, pady=2, sticky="ew")
                self.button2.grid(row=2, column=0, columnspan=2, pady=2, sticky="n")

                self.output_text1.grid(row=3, column=0, columnspan=2, pady=5, sticky="nsew")


        elif button_type == "Password_Confirm":
            bind_password_value = self.entry2.get().strip()
            if not bind_password_value:
                self.output_text1.insert(tk.END, "Your password is empty\n")
            else:
                self.bind_password = bind_password_value
                self.config_messagge(f"Bind Password: {self.bind_password}\n")
                self.output_text1.insert(tk.END, f"Password set\n")
                self.oath_data.append(f"bind_password: {self.bind_password}")

                
                self.label2.grid_forget()
                self.entry2.grid_forget()
                self.button2.grid_forget()

                
                self.label3.grid(row=0, column=0, columnspan=2, pady=(5, 2), sticky="n")
                self.entry3.grid(row=1, column=0, columnspan=2, pady=2, sticky="ew")
                self.button3.grid(row=2, column=0, columnspan=2, pady=2, sticky="n")

                self.output_text1.grid(row=3, column=0, columnspan=2, pady=5, sticky="nsew")


        elif button_type == "Base_DN_Confirm":
            base_dn_value = self.entry3.get().strip()
            if not base_dn_value:
                self.output_text1.insert(tk.END, "Base domain name and OU not entered\n")
            else:
                self.base_dn = base_dn_value
                self.config_messagge(f"Base DN: {self.base_dn}\n")
                self.output_text1.insert(tk.END, f"Base DN set to: {self.base_dn}\n")
                self.oath_data.append(f"base_dn: {self.base_dn}")

                
                self.label3.grid_forget()
                self.entry3.grid_forget()
                self.button3.grid_forget()
                
                # Show next set (Filter)
                self.label4.grid(row=0, column=0, columnspan=2, pady=(5, 2), sticky="n")
                self.entry4.grid(row=1, column=0, columnspan=2, pady=2, sticky="ew")
                self.button4.grid(row=2, column=0, columnspan=2, pady=2, sticky="n")

                self.output_text1.grid(row=3, column=0, columnspan=2, pady=5, sticky="nsew")


        elif button_type == "Filter_Confirm":
            filter_value = self.entry4.get().strip()
            if not filter_value:
                self.output_text1.insert(tk.END, "Filter not entered\n")
            else:
                self.filter = filter_value
                self.config_messagge(f"Filter: {self.filter}\n")
                self.output_text1.insert(tk.END, f"Filter set to: {self.filter}\n")
                self.oath_data.append(f"filter: {self.filter}")

                self.label4.grid_forget()
                self.entry4.grid_forget()
                self.button4.grid_forget()
                
                self.output_text1.insert(tk.END, "\nAll LDAP configuration data collected!\n")
                self.output_text1.insert(tk.END, f"LDAP Server: {self.ldap_server}\n")
                self.output_text1.insert(tk.END, f"Bind DN: {self.bind_dn}\n")
                self.output_text1.insert(tk.END, f"Bind Password: {'*' * len(self.bind_password)}\n") 
                self.output_text1.insert(tk.END, f"Base DN: {self.base_dn}\n")
                self.output_text1.insert(tk.END, f"Filter: {self.filter}\n")
                
                self.done_button = tk.Button(self.root, text="Done", command=self.destroy, 
                                                     font=('Arial', 9), width=8, relief="raised")
                self.done_button.pack(pady=10) 

                self.output_text1.grid(row=0, column=0, columnspan=2, pady=5, sticky="nsew") 

        self.output_text1.see(tk.END)
    
class LDAuthCh(tk.Toplevel):
    def __init__(self, master=None, pas=None):
        super().__init__(master)
        self.root = self
        self.log_file_name = "ldap.log"
        self.log_pass = m.get_log_file_path(self.log_file_name)
        self.config_file_name = "ldap_config.cfg"
        self.ldap_conf_pass = pas
        self.del_folder()
        print(pas)
        self.ldap_server = 'ldap://' 
        self.bind_dn = '' 
        self.bind_password = ''
        self.base_dn = ''
        self.filter = '' 
        self.title("LDAP OAUth")
        self.geometry("350x350") 
        self.resizable(False, False)
        self.config(bg="grey")
        
        style = ttk.Style(self)
        style.configure("Custom.TLabel", background="grey", foreground="black", font=('Arial',10)) 
        
        main_frame = ttk.Frame(self, style="Custom.TLabel", relief="flat", borderwidth=0)
        main_frame.pack(expand=True, padx=10, pady=10) 
        
        self.label = ttk.Label(main_frame, text="Type ldap_server", style="Custom.TLabel")
        self.entry = ttk.Entry(main_frame)
        self.button = tk.Button(main_frame, text="Confirm", command=lambda: self.on_button_click("Ldap_server_Confirm"),
                                 font=('Arial', 9), width=8, relief="raised")
        self.entry.bind("<Return>", lambda event: self.on_button_click("Ldap_server_Confirm"))

        self.label1 = ttk.Label(main_frame, text="Type ldap_DN", style="Custom.TLabel")
        self.entry1 = ttk.Entry(main_frame)
        self.button1 = tk.Button(main_frame, text="Confirm", command=lambda: self.on_button_click("LDAP_DN_Confirm"),
                                 font=('Arial', 9), width=8, relief="raised")
        self.entry1.bind("<Return>", lambda event: self.on_button_click("LDAP_DN_Confirm"))

        self.label2 = ttk.Label(main_frame, text="Type admin ldap password", style="Custom.TLabel")
        self.entry2 = ttk.Entry(main_frame, show="*") 
        self.button2 = tk.Button(main_frame, text="Confirm", command=lambda: self.on_button_click("Password_Confirm"),
                                 font=('Arial', 9), width=8, relief="raised")
        self.entry2.bind("<Return>", lambda event: self.on_button_click("Password_Confirm"))

        self.label3 = ttk.Label(main_frame, text="Type Ldap Base DN", style="Custom.TLabel") 
        self.entry3 = ttk.Entry(main_frame)
        self.button3 = tk.Button(main_frame, text="Confirm", command=lambda: self.on_button_click("Base_DN_Confirm"),
                                 font=('Arial', 9), width=8, relief="raised")
        self.entry3.bind("<Return>", lambda event: self.on_button_click("Base_DN_Confirm"))

        # Corrected label text for the filter input
        self.label4 = ttk.Label(main_frame, text="Type Ldap Filter", style="Custom.TLabel") 
        self.entry4 = ttk.Entry(main_frame)
        self.button4 = tk.Button(main_frame, text="Confirm", command=lambda: self.on_button_click("Filter_Confirm"),
                                 font=('Arial', 9), width=8, relief="raised")
        self.entry4.bind("<Return>", lambda event: self.on_button_click("Filter_Confirm"))
    
        self.output_text1 = ScrolledText(main_frame, wrap=tk.WORD, height=5, width=40, font=('Arial', 9))

        
        self.label.grid(row=0, column=0, columnspan=2, pady=(5, 2), sticky="n")
        self.entry.grid(row=1, column=0, columnspan=2, pady=2, sticky="ew")
        self.button.grid(row=2, column=0, columnspan=2, pady=2, sticky="n")
        
        
        self.output_text1.grid(row=3, column=0, columnspan=2, pady=5, sticky="nsew")
        main_frame.grid_rowconfigure(3, weight=1) 
        main_frame.grid_columnconfigure(0, weight=1)
        self.grab_set()
        self.focus_set()
        self.transient(master)
        self.wait_window()
    def config_messagge(self,message):
        
        """ Writes config to the specified config file. """
        try:
            with open(self.ldap_conf_pass, 'a', encoding='utf-8') as conf_f:
                conf_f.write(message)
        except Exception as e:
            print(f"Error writing to conf file: {e}")
        
    def on_button_click(self, button_type):
            
            
        self.output_text1.delete(1.0, tk.END) 
        self.oath_data = list()
        if button_type == "Ldap_server_Confirm":
            ldap_server_value = self.entry.get().strip()
            if not ldap_server_value:
                self.output_text1.insert(tk.END, "LDAP server wasn't entered\n")
            else:
                self.ldap_server = 'ldap://' + ldap_server_value
                self.config_messagge(f"LDAP server: {self.ldap_server}\n")
                self.output_text1.insert(tk.END, f"LDAP server set to: {self.ldap_server}\n")
                self.oath_data.append(f"ldap_server: {self.ldap_server}")

                
                self.label.grid_forget()
                self.entry.grid_forget()
                self.button.grid_forget()

                
                self.label1.grid(row=0, column=0, columnspan=2, pady=(5, 2), sticky="n")
                self.entry1.grid(row=1, column=0, columnspan=2, pady=2, sticky="ew")
                self.button1.grid(row=2, column=0, columnspan=2, pady=2, sticky="n")
                
                
                self.output_text1.grid(row=3, column=0, columnspan=2, pady=5, sticky="nsew")


        elif button_type == "LDAP_DN_Confirm":
            bind_dn_value = self.entry1.get().strip()
            if not bind_dn_value:
                self.output_text1.insert(tk.END, "CN DN wasn't entered\n")
            else:
                self.bind_dn = bind_dn_value
                self.config_messagge(f"Bind DN: {self.bind_dn}\n")
                self.output_text1.insert(tk.END, f"LDAP DN set to: {self.bind_dn}\n")
                self.oath_data.append(f"bind_dn: {self.bind_dn}")

                
                self.label1.grid_forget()
                self.entry1.grid_forget()
                self.button1.grid_forget()

                
                self.label2.grid(row=0, column=0, columnspan=2, pady=(5, 2), sticky="n")
                self.entry2.grid(row=1, column=0, columnspan=2, pady=2, sticky="ew")
                self.button2.grid(row=2, column=0, columnspan=2, pady=2, sticky="n")

                self.output_text1.grid(row=3, column=0, columnspan=2, pady=5, sticky="nsew")


        elif button_type == "Password_Confirm":
            bind_password_value = self.entry2.get().strip()
            if not bind_password_value:
                self.output_text1.insert(tk.END, "Your password is empty\n")
            else:
                self.bind_password = bind_password_value
                self.config_messagge(f"Bind Password: {self.bind_password}\n")
                self.output_text1.insert(tk.END, f"Password set\n")
                self.oath_data.append(f"bind_password: {self.bind_password}")

                
                self.label2.grid_forget()
                self.entry2.grid_forget()
                self.button2.grid_forget()

                
                self.label3.grid(row=0, column=0, columnspan=2, pady=(5, 2), sticky="n")
                self.entry3.grid(row=1, column=0, columnspan=2, pady=2, sticky="ew")
                self.button3.grid(row=2, column=0, columnspan=2, pady=2, sticky="n")

                self.output_text1.grid(row=3, column=0, columnspan=2, pady=5, sticky="nsew")


        elif button_type == "Base_DN_Confirm":
            base_dn_value = self.entry3.get().strip()
            if not base_dn_value:
                self.output_text1.insert(tk.END, "Base domain name and OU not entered\n")
            else:
                self.base_dn = base_dn_value
                self.config_messagge(f"Base DN: {self.base_dn}\n")
                self.output_text1.insert(tk.END, f"Base DN set to: {self.base_dn}\n")
                self.oath_data.append(f"base_dn: {self.base_dn}")

                
                self.label3.grid_forget()
                self.entry3.grid_forget()
                self.button3.grid_forget()
                
                # Show next set (Filter)
                self.label4.grid(row=0, column=0, columnspan=2, pady=(5, 2), sticky="n")
                self.entry4.grid(row=1, column=0, columnspan=2, pady=2, sticky="ew")
                self.button4.grid(row=2, column=0, columnspan=2, pady=2, sticky="n")

                self.output_text1.grid(row=3, column=0, columnspan=2, pady=5, sticky="nsew")


        elif button_type == "Filter_Confirm":
            filter_value = self.entry4.get().strip()
            if not filter_value:
                self.output_text1.insert(tk.END, "Filter not entered\n")
            else:
                self.filter = filter_value
                self.config_messagge(f"Filter: {self.filter}\n")
                self.output_text1.insert(tk.END, f"Filter set to: {self.filter}\n")
                self.oath_data.append(f"filter: {self.filter}")

                self.label4.grid_forget()
                self.entry4.grid_forget()
                self.button4.grid_forget()
                
                self.output_text1.insert(tk.END, "\nAll LDAP configuration data collected!\n")
                self.output_text1.insert(tk.END, f"LDAP Server: {self.ldap_server}\n")
                self.output_text1.insert(tk.END, f"Bind DN: {self.bind_dn}\n")
                self.output_text1.insert(tk.END, f"Bind Password: {'*' * len(self.bind_password)}\n") 
                self.output_text1.insert(tk.END, f"Base DN: {self.base_dn}\n")
                self.output_text1.insert(tk.END, f"Filter: {self.filter}\n")
                
                self.done_button = tk.Button(self.root, text="Done", command=self.destroy, 
                                                     font=('Arial', 9), width=8, relief="raised")
                self.done_button.pack(pady=10) 

                self.output_text1.grid(row=0, column=0, columnspan=2, pady=5, sticky="nsew") 

        self.output_text1.see(tk.END)
    
    def del_folder(self):
        try:
            os.remove(self.ldap_conf_pass)
            print(f"Файл '{self.ldap_conf_pass}' успешно удален.🗑️")
        except FileNotFoundError:
            print(f"Ошибка: Файл '{self.ldap_conf_pass}' не найден.")
        except PermissionError:
            print(f"Ошибка: Недостаточно прав для удаления файла '{self.ldap_conf_pass}'.")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка при удалении файла: {e}")
        
def run_standalone_tester():
    
    root_for_standalone = tk.Tk()
    root_for_standalone.withdraw() 

    app_tester = LDAuth(root_for_standalone) 
    
    app_tester.protocol("WM_DELETE_WINDOW", lambda: on_standalone_close(app_tester, root_for_standalone))
    
    root_for_standalone.mainloop() 

def on_standalone_close(toplevel_window, root_window):

    toplevel_window.destroy()
    root_window.destroy()

if __name__ == "__main__":
    run_standalone_tester() 
