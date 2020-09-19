import tkinter as tk
import mysql.connector
from db import *
from PIL import ImageTk, Image
from functools import partial
from datetime import date,timedelta
import datetime
from tkcalendar import Calendar,DateEntry

class bookingpage(tk.Tk):
    def __init__(self,id, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Booking")
        self.geometry("900x500")
        self.config(background="black", pady=10)

        lbs = tk.Label(self, text="Booking", bg="black", fg="white", font=20)
        lbs.place(x=110, y=5)
        self.id=id
        self.details()
    def details(self):
        lb2_name = tk.Label(self, text="Name - ", bg="black", fg="white")
        self.name = tk.Entry(self)
        lb2_name.place(x=10, y=40)
        self.name.place(x=110, y=40)

        lb2_guest = tk.Label(self, text="No of Guest ", bg="black", fg="white")
        self.guest = tk.Entry(self)
        lb2_guest.place(x=10, y=80)
        self.guest.place(x=110, y=80)

        self.tkvar = tk.StringVar(self)

        # Dictionary with options

        choice = {'Standard', 'Deluxe', 'Luxury'}
        self.tkvar.set('Select')  # set the default option

        popupMenu = tk.OptionMenu(self, self.tkvar, *choice,command=self.check_acc)
        tk.Label(self, text="Room Type",bg="black", fg="white").place(x=10, y=120)
        popupMenu.place(x=110, y=120)

        lb2_room = tk.Label(self, text="No Of Room - ", bg="black", fg="white")
        self.room = tk.Entry(self)
        lb2_room.place(x=10, y=160)
        self.room.place(x=110, y=160)

        # lb2_s = tk.Label(self, text="Email - ", bg="black", fg="white")
        # self.lb2_s2 = tk.Entry(self)
        # lb2_s.place(x=10, y=200)
        # self.lb2_s2.place(x=110, y=200)

        current_date = date.today()
        self.cur_date=current_date
        tomorrow = date.today() + timedelta(1)
        label1 = tk.Label(self, text='Check In Date',bg="black", fg="white")
        label1.place(x='10', y='200')
        self.cal = DateEntry(self, width=12, year=current_date.year, month=current_date.month, day=current_date.day,
                             mindate=current_date, date_pattern='y-mm-dd',
                             background='darkblue', foreground='white', borderwidth=2)
        self.cal.place(x='110', y='200')
        label2 = tk.Label(self, text='Check out Date',bg="black", fg="white")
        label2.place(x='240', y='200')
        self.cal.bind("<<DateEntrySelected>>", self.callback)
        date_time_obj = datetime.datetime.strptime(self.cal.get(), '%Y-%m-%d')
        # print(type(date_time_obj))
        # if self.cal.get():
        #     min_date=self.cal.get()
        # else:
        #    min_date=tomorrow
        lb2_s = tk.Label(self, text="Price - ", bg="black", fg="white")
        self.price = tk.Label(self,bg="black", fg="white")
        lb2_s.place(x=10, y=240)
        self.price.place(x=110, y=240)
        self.cal1 = DateEntry(self, width=12, year=tomorrow.year, month=tomorrow.month, day=tomorrow.day,
                              mindate=tomorrow, date_pattern='y-mm-dd',
                              background='darkblue', foreground='white', borderwidth=2)
        self.cal1.place(x='380', y='200')
        # reg = self.register(self.callback)
        #
        # self.cal1.config(validate="key",
        #          validatecommand=(reg, '% P'))
        # button = tk.Button(self, text='Search', command=self.search)
        # button.place(x='150', y='120')
        try:

            mycursor = mydb.cursor()

            mycursor.execute("SELECT * FROM hotel_name where id=%s"%self.id)

            self.myresult = mycursor.fetchall()
            print(self.myresult)
            im = Image.open(r"%s" % self.myresult[0][5])
            image = im
            self.background_image = ImageTk.PhotoImage(im)
            lb_hotel = tk.Label(self, text=self.myresult[0][1], bg="black", fg="white", font=20)
            lb_hotel.place(x=400, y=40)
            row = 50
            lb_img = tk.Label(self,image=self.background_image,height=50,width=50)
            lb_img.place(x=400, y=80)
            lb_img.photo=self.background_image



        except:
           print("No result")
        button = tk.Button(self, text="book", command=self.book)
        button.place(x='120', y='280')

    def callback(self,input):
        w = input.widget
        date = w.get_date()+timedelta(1)
        self.cal1.config(mindate=date)

    def book(self):
        try:
            mycursor = mydb.cursor()

            sql = "INSERT INTO booking (name,no_guest,room_type,checkin,checkout,hot_name,book_date,total) VALUES (%s, %s,%s,%s,%s,%s,%s,%s)"
            val = (
                self.name.get(), self.guest.get(), self.tkvar.get(), self.cal.get(), self.cal1.get(), self.myresult[0][1],self.cur_date,(self.p*int(self.room.get())))
            mycursor.execute(sql, val)

            mydb.commit()

            print(mycursor.rowcount, "record inserted.")
            self.display=tk.Label(self)
            self.display2.config(bg="green", fg="white", text="Saved Success")

            self.display2.place(x=20, y=1)
        except:
            self.display = tk.Label(self)
            self.display2.config(bg="red", fg="white", text="Not Saved")

            self.display2.place(x=20, y=1)



    def check_acc(self,event):
        selected = self.tkvar.get()
        self.dic={'Standard':7,'Deluxe':8,'Luxury':9}
        self.dic2 = {'Standard': 2, 'Deluxe': 3, 'Luxury': 4}
        if(self.myresult[0][self.dic2[selected]]==0):
            lab=tk.Label(self,text="Room Full")
            lab.place(x=200,y=120)
        else:
            if (len(selected) != 0):
                self.price.config(text=self.myresult[0][self.dic[selected]], bg="black", fg="white")
                self.p=self.myresult[0][self.dic[selected]]
                # print(self.p)





        # if selected == "Kill":
        #     goal_label['text'] = "Required Kills"
        # elif selected == "Explore":
        #     goal_label['text'] = "Location ID"
        # elif selected == "Conversation":
        #     goal_label['text'] = "NPC ID"

if __name__ == "__main__":
    app = bookingpage()
    app.mainloop()




