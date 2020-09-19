import tkinter as tk
from admin_dashboard import *

class adminlogin(tk.Tk):
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        # self = Tk()
        self.title("Admin")
        self.geometry("900x500")
        self.config(background="black", pady=10)

        lb1 = tk.Label(self, text="Admin Login Form", bg="black", fg="white", font=20)
        lb1.place(x=110, y=5)

        lb2_u = tk.Label(self, text="Username - ", bg="black", fg="white")
        self.lb2_u2 = tk.Entry(self)
        lb2_u.place(x=10, y=40)
        self.lb2_u2.place(x=110, y=40)

        lb2_p = tk.Label(self, text="Password - ", bg="black", fg="white")
        self.lb2_p2 = tk.Entry(self,show='*')
        lb2_p.place(x=10, y=80)
        self.lb2_p2.place(x=110, y=80)

        self.display = tk.Label(self, text="Access : ", bg="black")
        self.display.place(x='100',y='160')

        bt = tk.Button(self, text="Login",command=self.dis)
        # bt.config(command=dis)
        bt.place(x=110, y=120)


    def dis(self):
         user = self.lb2_u2.get()
         pas = self.lb2_p2.get()
         if (user=='Hotel')and(pas=='Hotel@123'):
             self.destroy()
             a=admindash()
             # self.display.config(bg="green", fg="white", text="Access :Granted")
             # break
         else:
             print('denied')
             self.display.config(bg="red", fg="white", text="Access :Denied")









if __name__ == "__main__":
    app = adminlogin()
    app.mainloop()