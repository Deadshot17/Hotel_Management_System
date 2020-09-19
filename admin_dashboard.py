import tkinter as tk
from addroom import *
from editpage import*
from viewbooking import *

class admindash(tk.Tk):
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        # self = Tk()
        self.title("Dashboard")
        self.geometry("900x500")
        self.config(background="black", pady=10)
        lb1 = tk.Label(self, text="Admin Dashboard", bg="black", fg="white", font=20)
        lb1.place(x=110, y=5)
        self.button=tk.Button(self,text='Add Room',command=self.addroom)
        self.button.place(x='150',y='120')
        self.button3 = tk.Button(self, text='Edit Room Data',command=self.editdata)
        self.button3.place(x='150', y='160')
        self.button2 = tk.Button(self, text='View Booking',command=self.booking)
        self.button2.place(x='150', y='200')

        self.button.bind("<Enter>", self.on_enter)
        self.button.bind("<Leave>", self.on_leave)

        self.button2.bind("<Enter>", self.on_enter2)
        self.button2.bind("<Leave>", self.on_leave2)

        self.button3.bind("<Enter>", self.on_enter3)
        self.button3.bind("<Leave>", self.on_leave3)

    def on_enter(self, e):
        self.button['background'] = 'green'
        self.button['width'] = 20

    def on_leave(self, e):
        self.button['background'] = 'SystemButtonFace'
        self.button['width'] = 10

    def on_enter2(self, e):
        self.button2['background'] = 'green'
        self.button2['width'] = 20

    def on_leave2(self, e):
        self.button2['background'] = 'SystemButtonFace'
        self.button2['width'] = 10


    def on_enter3(self, e):
        self.button3['background'] = 'green'
        self.button3['width'] = 20

    def on_leave3(self, e):
        self.button3['background'] = 'SystemButtonFace'
        self.button3['width'] = 13

    def addroom(self):
        self.destroy()
        add=addroom()

    def editdata(self):
        self.destroy()
        # self.withdraw()
        edit=editpage()



    def booking(self):
        self.destroy()
        book=viewbooking()


if __name__ == "__main__":
    app = admindash()
    app.mainloop()