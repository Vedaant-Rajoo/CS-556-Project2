import customtkinter as tk
from tkinter import messagebox as mb
from scripts.login import login
class LoginFrame(tk.CTkFrame):
    def __init__(self, master=None,on_login=None):
        super().__init__(master=master)

        self.on_login = on_login

        self.master = master
        self.master.title("Login")
        self.master.minsize(300, 200)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        self.username_label = tk.CTkLabel(master=self, text="Username:")
        self.username_label.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="nsew")
        self.username_entry = tk.CTkEntry(master=self)
        self.username_entry.grid(row=0, column=1, padx=20, pady=(20, 0), sticky="nsew")

        self.password_label = tk.CTkLabel(master=self, text="Password:")
        self.password_label.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        self.password_entry = tk.CTkEntry(master=self, show="*")
        self.password_entry.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

        self.login_button = tk.CTkButton(master=self, text="Login", command=self.login)
        self.login_button.grid(row=2, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if login(username, password) is True:
            if self.on_login is not None:
                self.on_login(username)   
        else:
            self.username_entry.delete(0, "end")
            self.password_entry.delete(0, "end")
            mb.showwarning("Error", "Invalid username or password")
