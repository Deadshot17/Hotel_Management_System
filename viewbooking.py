import tkinter as tk
import mysql.connector
from db import *
from PIL import ImageTk, Image
from functools import partial
from booking_page import*

class viewbooking(tk.Tk):
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("View Booking")
        self.geometry("900x500")
        self.config(background="black", pady=10)

        lb1 = tk.Label(self, text="View Bookings", bg="black", fg="white", font=20)
        lb1.place(x=110, y=5)
        self.tkvar = tk.StringVar(self)
        choice = {'Name', 'Date Of Booking', 'No of guest','check in date','check out date'}
        self.tkvar.set('Select')  # set the default option

        popupMenu = tk.OptionMenu(self, self.tkvar, *choice, command=self.check_acc)
        tk.Label(self, text="Filter", bg="black", fg="white").place(x=10, y=35)
        popupMenu.place(x=80, y=35)
        lb2_s=tk.Label(self, text="Value", bg="black", fg="white")
        self.val = tk.Entry(self)
        lb2_s.place(x=200, y=35)
        self.val.place(x=260, y=35)


        self.data()

    def check_acc(self,event):
        # self.widgets.clear()
        print(self.widgets)
        if 1 in self.widgets.keys():
            self.widgets[1]['name'].destroy()
            self.widgets[1]['no_of_guest'].destroy()
            self.widgets[1]['rtype'].destroy()
            self.widgets[1]['check_in'].destroy()
            self.widgets[1]['hotel_name'].destroy()
            self.widgets[1]['date_of_booking'].destroy()
            self.widgets[1]['amount'].destroy()
        if 2 in self.widgets.keys():
            self.widgets[2]['name'].destroy()
            self.widgets[2]['no_of_guest'].destroy()
            self.widgets[2]['rtype'].destroy()
            self.widgets[2]['check_in'].destroy()
            self.widgets[2]['hotel_name'].destroy()
            self.widgets[2]['date_of_booking'].destroy()
            self.widgets[2]['amount'].destroy()


        selected = self.tkvar.get()
        value=self.val.get()
        # print(value)
        if(len(selected)!=0)and(len(value)!=0):
            self.widgets = {}
            dic={'Name':'name','Date Of Booking':'book_date','No of guest':'no_guest','check in date':'checkin', 'check out date':'checkout'}
            # print(widgets)
            try:
                mycursor = mydb.cursor()

                mycursor.execute("SELECT * FROM booking WHERE %s='%s'"%(dic[selected],value))

                myresult = mycursor.fetchall()
                # print(myresult)
                # lb1 = tk.Label(self, text="Hotels", bg="black", fg="white", font=20)
                # lb1.place(x=110, y=50)
                # row = 50
                lab1 = tk.Label(self, text="Visitor", bg="black", fg="white")
                lab1.place(x=10, y=90)
                lab2 = tk.Label(self, text="No", bg="black", fg="white")
                lab2.place(x=90, y=90)
                lab3 = tk.Label(self, text="Room Type", bg="black", fg="white")
                lab3.place(x=170, y=90)
                lab4 = tk.Label(self, text="Check in", bg="black", fg="white")
                lab4.place(x=250, y=90)
                lab5 = tk.Label(self, text="Hotel Name", bg="black", fg="white")
                lab5.place(x=330, y=90)
                lab6 = tk.Label(self, text="Book Date", bg="black", fg="white")
                lab6.place(x=410, y=90)
                lab7 = tk.Label(self, text="Amount", bg="black", fg="white")
                lab7.place(x=500, y=90)
                row = 90

                for x in myresult:

                    print(x)
                    row += 50
                    id = x[0]
                    # print(x[0])

                    # print(background_image)
                    # lb1 = tk.Label(self, text=x[1],image=background_image)
                    # lb1.place(x=110, y=67)
                    # call_result = partial(self.book, id)
                    self.widgets[x[0]] = {
                        "name": tk.Label(self, text=x[1], bg='black', fg="white"),
                        "no_of_guest": tk.Label(self, text=x[2], bg='black', fg="white"),
                        "rtype": tk.Label(self, text=x[3], bg='black', fg="white"),
                        "check_in": tk.Label(self, text=x[4], bg='black', fg="white"),
                        "hotel_name": tk.Label(self, text=x[6], bg='black', fg="white"),
                        "date_of_booking": tk.Label(self, text=x[7], bg='black', fg="white"),
                        "amount": tk.Label(self, text=x[8], bg='black', fg="white"),

                    }
                    # # self.widgets[x[0]]["name"].photo = self.background_image
                    self.widgets[x[0]]["name"].place(x=10, y=row)
                    self.widgets[x[0]]["no_of_guest"].place(x=90, y=row)
                    self.widgets[x[0]]["rtype"].place(x=170, y=row)
                    self.widgets[x[0]]["check_in"].place(x=250, y=row)
                    self.widgets[x[0]]["hotel_name"].place(x=330, y=row)
                    self.widgets[x[0]]["date_of_booking"].place(x=410, y=row)
                    self.widgets[x[0]]["amount"].place(x=500, y=row)
            except:
                print('no res')





    def data(self):
        try:
            mycursor = mydb.cursor()

            mycursor.execute("SELECT * FROM booking")

            myresult = mycursor.fetchall()
            # print(myresult)
            # lb1 = tk.Label(self, text="Hotels", bg="black", fg="white", font=20)
            # lb1.place(x=110, y=50)
            # row = 50
            lab1=tk.Label(self,text="Visitor", bg="black", fg="white")
            lab1.place(x=10,y=90)
            lab2 = tk.Label(self, text="No", bg="black", fg="white")
            lab2.place(x=90,y=90)
            lab3 = tk.Label(self, text="Room Type", bg="black", fg="white")
            lab3.place(x=170,y=90)
            lab4 = tk.Label(self, text="Check in", bg="black", fg="white")
            lab4.place(x=250,y=90)
            lab5 = tk.Label(self, text="Hotel Name", bg="black", fg="white")
            lab5.place(x=330,y=90)
            lab6 = tk.Label(self, text="Book Date", bg="black", fg="white")
            lab6.place(x=410,y=90)
            lab7 = tk.Label(self, text="Amount", bg="black", fg="white")
            lab7.place(x=500,y=90)
            row=90
            self.widgets = {}
            for x in myresult:
                # print(x)
                row += 50
                id =x[0]
                # print(x[0])

                # print(background_image)
                # lb1 = tk.Label(self, text=x[1],image=background_image)
                # lb1.place(x=110, y=67)
                # call_result = partial(self.book, id)
                self.widgets[x[0]] = {
                    "name": tk.Label(self, text=x[1], bg='black', fg="white"),
                    "no_of_guest": tk.Label(self, text=x[2], bg='black', fg="white"),
                    "rtype": tk.Label(self, text=x[3], bg='black', fg="white"),
                    "check_in": tk.Label(self, text=x[4], bg='black', fg="white"),
                    "hotel_name": tk.Label(self, text=x[6], bg='black', fg="white"),
                    "date_of_booking": tk.Label(self, text=x[7], bg='black', fg="white"),
                    "amount": tk.Label(self, text=x[8], bg='black', fg="white"),

                }
                # # self.widgets[x[0]]["name"].photo = self.background_image
                self.widgets[x[0]]["name"].place(x=10, y=row)
                self.widgets[x[0]]["no_of_guest"].place(x=90, y=row)
                self.widgets[x[0]]["rtype"].place(x=170, y=row)
                self.widgets[x[0]]["check_in"].place(x=250, y=row)
                self.widgets[x[0]]["hotel_name"].place(x=330, y=row)
                self.widgets[x[0]]["date_of_booking"].place(x=410, y=row)
                self.widgets[x[0]]["amount"].place(x=500, y=row)
        except:
            print("No result")
if __name__ == "__main__":
    app = viewbooking()
    app.mainloop()
