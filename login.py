import tkinter as tk
from register import *
from roomsearch import *
import db

class login_form(tk.Tk):
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        # self = Tk()
        self.title("Visitor")
        self.geometry("900x500")
        self.config(background="black", pady=10)

        lb1 = tk.Label(self, text="Login Form", bg="black", fg="white", font=20)
        lb1.place(x=110, y=5)

        lb2_u = tk.Label(self, text="Email - ", bg="black", fg="white")
        self.lb2_u2 = tk.Entry(self)
        lb2_u.place(x=10, y=40)
        self.lb2_u2.place(x=110, y=40)

        lb2_p = tk.Label(self, text="Password - ", bg="black", fg="white")
        self.lb2_p2 = tk.Entry(self)
        lb2_p.place(x=10, y=80)
        self.lb2_p2.place(x=110, y=80)

        self.display = tk.Label(self, text="Access : ", bg="black")

        bt = tk.Button(self, text="Login",command=self.dis)
        # bt.config(command=dis)
        bt.place(x=110, y=120)
        bt2 = tk.Button(self, text="SignUp", command=self.newsign)
        bt2.place(x=170, y=120)

    def dis(self):
         user = self.lb2_u2.get()
         print(user)
         pas = self.lb2_p2.get()
         try:

             mycursor = mydb.cursor()

             # print(mycursor.execute("SELECT * FROM register where name=%s" %user))
             mycursor.execute("SELECT * FROM register")

             self.myresult = mycursor.fetchall()
             for res in self.myresult:
                 if (res[2]==user)and (res[4]==pas):
                     self.destroy()
                     a=rsearch()

                     # print('grant')
                     break
                 else:
                     print('denied')
                     self.display.config(bg="green", fg="white", text="Access :Denied")
                     self.display.place(x=0, y=5)




             # if user ==self.myresult :
             #     self.display.config(bg="green", fg="white", text="Access :Granted")
             #     break
             # else:
             #     self.display.config(bg="red", fg="white", text="Access :Denied")
             #



         except:
             self.display.config(bg="green", fg="white", text="Enter all values")
             self.display.place(x=0, y=5)




    def newsign(self):
        # self.destroy()
        registeration=register()
        registeration.newsign()







if __name__ == "__main__":
    app = login_form()
    app.mainloop()