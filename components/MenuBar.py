import tkinter as tk

class MenuBar(tk.Menu):
    def __init__(self,master=None,on_logout=None,on_Logs=None):
        super().__init__(master=master)
        self.on_logout = on_logout
        self.on_Logs = on_Logs
        self.master = master
        self.add_command(label="LogOut", command=self.logout)
        self.add_command(label="Logs", command=self.goToLogs)
        self.add_separator()
        
    def logout(self):
        if self.on_logout is not None:
            self.on_logout()
    def goToLogs(self):
        if self.on_Logs is not None:
            self.on_Logs()
    
