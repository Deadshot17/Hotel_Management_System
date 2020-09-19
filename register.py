from login import *
import tkinter as tk
import mysql.connector
from db import *

class register(tk.Tk):
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("SignUp")
        self.geometry("900x500")
        self.config(background="black", pady=10)
        self.newsign()

    def newsign(self):            
            

            lbs = tk.Label(self, text="SignUp", bg="black", fg="white", font=20)
            lbs.place(x=110, y=5)

            lb2_s = tk.Label(self, text="Name - ", bg="black", fg="white")
            self.name = tk.Entry(self)
            lb2_s.place(x=10, y=40)
            self.name.place(x=110, y=40)
            lb2_s = tk.Label(self, text="Email - ", bg="black", fg="white")
            self.email = tk.Entry(self)
            lb2_s.place(x=10, y=80)
            self.email.place(x=110, y=80)

            self.old_value = ''

            self.phone = tk.StringVar()
            lb2_s = tk.Label(self, text="Phone - ", bg="black", fg="white")
            self.ph = tk.Entry(self,textvariable=self.phone)
            self.phone.trace('w', self.check)
            lb2_s.place(x=10, y=120)
            self.ph.place(x=110, y=120)

            lb2_ps = tk.Label(self, text="Password - ", bg="black", fg="white")
            self.lb2_ps2 = tk.Entry(self,show='*')
            lb2_ps.place(x=10, y=160)
            self.lb2_ps2.place(x=110, y=160)

            self.dis = tk.Label(self, text="", bg="black", fg="white")
            self.dis.place(x=100, y=150)
            bts = tk.Button(self, text="Register", command=self.reg)
            bts.place(x=110, y=200)
            bts = tk.Button(self, text="Login", command=self.login)
            bts.place(x=210, y=200)

    def login(self):
        self.destroy()
        a=login_form()



    def check(self, *args):
        if self.phone.get().isdigit():
            # the current value is only digits; allow this
            self.old_value = self.phone.get()

        else:
            # there's non-digit characters in the input; reject this
            self.phone.set(self.old_value)

    def reg(self):
        try:
            mycursor = mydb.cursor()

            sql = "INSERT INTO register (name,email,phone,pass) VALUES (%s, %s,%s,%s)"
            val = (
                self.name.get(), self.email.get(), self.phone.get(), self.lb2_ps2.get())
            mycursor.execute(sql, val)

            mydb.commit()

            print(mycursor.rowcount, "record inserted.")
            self.display=tk.Label(self)
            self.display.config(bg="green", fg="white", text="Saved Success")

            self.display.place(x=20, y=1)
        except:
            self.display = tk.Label(self)
            self.display.config(bg="red", fg="white", text="Not Saved")

            self.display.place(x=20, y=1)
if __name__ == "__main__":
    app = register()
    app.mainloop()