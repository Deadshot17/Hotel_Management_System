# #!/usr/bin/python
import tkinter as tk
from adminlogin import*
from login import *
LARGEFONT =("Verdana", 25)

class main(tk.Tk):
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        # a=login()

        self.title("Hotel Booking")
        self.geometry("900x500")
        self.config(background="black", pady=10)
        label = tk.Label(self, text='HOTEL MANAGEMENT SYSTEM', font=LARGEFONT,bg='black',fg='white')
        label.place(x=10,y=10)
        button= tk.Button(self,text='Visitor',command=self.login)
        button.place(x=120,y=80)



        button= tk.Button(self,text='Admin',command=self.admin)
        button.place(x=120,y=120)
    def login(self):
        self.destroy()
        a=login_form()
    def admin(self):
        self.destroy()
        a=adminlogin()

app = main()
app.mainloop()