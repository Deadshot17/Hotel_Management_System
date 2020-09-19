import tkinter as tk
import mysql.connector
from db import *
from PIL import ImageTk, Image
from functools import partial
from datetime import date,timedelta
import datetime
from tkcalendar import Calendar,DateEntry
from edit_room import *

class editpage(tk.Tk):
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk

        tk.Tk.__init__(self, *args, **kwargs)
        self.deiconify()
        self.title("Edit")
        self.geometry("900x500")
        self.config(background="black", pady=10)

        # lbs = tk.Label(self, text="", bg="black", fg="white", font=20)
        # lbs.place(x=110, y=5)
        self.id=id
        self.data()

    def data(self):
        try:
            mycursor = mydb.cursor()

            mycursor.execute("SELECT * FROM hotel_name")

            myresult = mycursor.fetchall()
            lb1 = tk.Label(self, text="Hotels", bg="black", fg="white", font=20)
            lb1.place(x=110, y=50)
            row = 50
            self.widgets = {}
            for x in myresult:
                print(x)
                row += 100
                id = x[0]
                print("r" + x[5])
                im = Image.open(r"%s" % x[5])
                image = im
                self.background_image = ImageTk.PhotoImage(im)
                # print(background_image)
                # lb1 = tk.Label(self, text=x[1],image=background_image)
                # lb1.place(x=110, y=67)
                call_result = partial(self.edit, x)
                self.widgets[x[0]] = {
                    "name": tk.Label(self, text=x[1], bg='black', fg="white", font=20),
                    "description": tk.Label(self, text=x[6], bg='black', fg="white", font=20),
                    "image": tk.Label(self, image=self.background_image, height=50, width=50),
                    "button": tk.Button(self, text="Edit", command=call_result),
                }
                self.widgets[x[0]]["image"].photo = self.background_image
                self.widgets[x[0]]["name"].place(x=200, y=row)
                self.widgets[x[0]]["description"].place(x=400, y=row)
                self.widgets[x[0]]["image"].place(x=40, y=row)
                self.widgets[x[0]]["button"].place(x=600, y=row)
        except:
            print("No result")

    def edit(self,data):
        self.withdraw()
        a= edit_room().editing(data)
if __name__ == "__main__":
    app = editpage()
    app.mainloop()