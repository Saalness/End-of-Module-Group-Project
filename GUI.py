import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('400x300')
        self.title('Client Server Programming')
        
        tk.Button(self, text='SERVER',width=30,bg='Pink',fg='Black',command = self.client).place(x=100,y=100)
        tk.Button(self, text='CLIENT',width=30,bg='Pink',fg='Black',command = self.server).place(x=100,y=200)
    def client(self):
        exec(open("client1.py").read())
    def server(self):
        exec(open("server1.py").read())
        
    

if __name__ == "__main__":
    app = App()
    app.mainloop()