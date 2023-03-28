import customtkinter as tk
import tkinter as ctk
from scripts.connect import *
class HomeFrame(tk.CTkFrame):
    def __init__(self, master=None,username=None):
        super().__init__(master=master)
        self.username = username
        self.welLabel = tk.CTkLabel(self, text=f"Welcome to the Home Page {self.username}!")
        self.welLabel.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        if isowner(self.username):
            self.adminLabel = ctk.StringVar(value="You own or curate a/some database(s).") 
            if isDBA(username=self.username):
                self.adminLabel.set(self.adminLabel.get() + " You are also a Database Administrator.")
            self.adminCtkLabel = tk.CTkLabel(self, textvariable=self.adminLabel)
            self.adminCtkLabel.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        else:
            if isDBA(username=self.username):
                self.adminLabel = ctk.StringVar(value="You are a Database Administrator.") 
                self.adminCtkLabel = tk.CTkLabel(self, textvariable=self.adminLabel)
                self.adminCtkLabel.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")