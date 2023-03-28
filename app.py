import customtkinter as tk
import tkinter as ctk
from tkinter import messagebox as mb
from components.HomeFrame import HomeFrame
from components.LoginFrame import LoginFrame
from scripts.connect import *
class App(tk.CTk):
    def __init__(self):
        super().__init__()
        self.minsize(600, 600)
        self.username = None

        self.my_menu = ctk.Menu(self)
        self.config(menu=self.my_menu)

        self.file_menu = ctk.Menu(self.my_menu)
        self.my_menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Logout", command=self.logout, state="disabled", accelerator="Ctrl+O")
        self.file_menu.add_command(label="Logs", command=self.goToLogs, state="disabled", accelerator="Ctrl+L")
        self.file_menu.add_command(label="Exit", command=self.quit, accelerator="Ctrl+Q")
        self.file_menu.add_separator()

        self.dba_menu = ctk.Menu(self.my_menu)
        self.my_menu.add_cascade(label="DBA", menu=self.dba_menu)
        self.dba_menu.add_command(label="Open Policy Editor", command= self.goToPolicyEditor, state="disabled", accelerator="Ctrl+P")
        
        self.admin_menu = ctk.Menu(self.my_menu)
        self.my_menu.add_cascade(label="Admin", menu=self.admin_menu)
        self.admin_menu.add_command(label="Open Admin Portal", command= self.goToAdminPortal, accelerator="Ctrl+U", state="disabled")

        self.login_frame = LoginFrame(self,on_login=self.show_home_frame)
        self.login_frame.pack()

        self.home_frame = HomeFrame(self)
        self.home_frame.pack_forget()

    def show_home_frame(self,username):
        self.username = username
        self.login_frame.pack_forget()
        self.home_frame = HomeFrame(self,username=username)
        self.home_frame.pack()

        self.file_menu.entryconfig("Logout", state="normal")
        self.file_menu.entryconfig("Logs", state="normal")
        if isDBA(self.username):
            self.dba_menu.entryconfig("Open Policy Editor", state="normal")
        if isowner(self.username):
            self.admin_menu.entryconfig("Open Admin Portal", state="normal")

    def logout(self):
        self.username = None
        self.home_frame.pack_forget()
        self.login_frame.pack()
        self.file_menu.entryconfig("Logout", state="disabled")
        self.file_menu.entryconfig("Logs", state="disabled")
        self.admin_menu.entryconfig("Open Admin Portal", state="disabled")
        self.dba_menu.entryconfig("Open Policy Editor", state="disabled")

    
    def goToLogs(self):
        mb.showinfo("Logs", "This is the Logs Page")

    def goToPolicyEditor(self):
        mb.showinfo("Policy Editor", "This is the Policy Editor Page")
    
    def goToAdminPortal(self):
        mb.showinfo("Admin Portal", "This is the Admin Portal Page")


if __name__ == "__main__":
    app = App()
    app.mainloop()