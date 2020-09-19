from booking import *
from tkcalendar import Calendar,DateEntry
import tkinter as tk
from datetime import date,timedelta
import datetime
# from register import *

class rsearch(tk.Tk):
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        # self = Tk()
        current_date = date.today()
        tomorrow = date.today() + timedelta(1)
        print(type(tomorrow))
        self.title("Search")
        self.geometry("900x500")
        self.config(background="black", pady=10)
        label1=tk.Label(self,text='Check In Date')
        label1.place(x='60',y='40')
        self.cal = DateEntry(self, width=12,year=current_date.year, month=current_date.month, day=current_date.day,mindate=current_date,date_pattern='y-mm-dd',
                        background='darkblue', foreground='white', borderwidth=2)
        self.cal.place(x='60',y='80')
        label2 = tk.Label(self, text='Check out Date')
        label2.place(x='200', y='40')
        self.cal.bind("<<DateEntrySelected>>", self.callback)
        date_time_obj = datetime.datetime.strptime(self.cal.get(), '%Y-%m-%d')
        print(type(date_time_obj))
        # if self.cal.get():
        #     min_date=self.cal.get()
        # else:
        #    min_date=tomorrow
        self.cal1 = DateEntry(self, width=12, year=tomorrow.year, month=tomorrow.month, day=tomorrow.day,mindate=tomorrow,date_pattern='y-mm-dd',
                        background='darkblue', foreground='white', borderwidth=2)
        self.cal1.place(x='200', y='80')
        # reg = self.register(self.callback)
        #
        # self.cal1.config(validate="key",
        #          validatecommand=(reg, '% P'))
        button=tk.Button(self,text='Search',command=self.search)
        button.place(x='150',y='120')
    def search(self):
        print(self.cal.get())
        print(self.cal1.get())
        self.destroy()
        bpage=booking()
    def callback(self,input):
        w = input.widget
        date = w.get_date()+timedelta(1)
        self.cal1.config(mindate=date)

if __name__ == "__main__":
      app=rsearch()
      app.mainloop()

