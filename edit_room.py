import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
from db import *
from admin_dashboard import*

class edit_room(tk.Tk):
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.file=''
        self.title("Edit Hotel")
        self.geometry("900x500")
        self.config(background="black", pady=10)
        lbs = tk.Label(self, text="Edit Hotel", bg="black", fg="white", font=20)
        lbs.place(x=110, y=15)

    def editing(self,data):
        if data:
            print(data)
            self.id=data[0]
            lb2_s = tk.Label(self, text="Hotel Name - ", bg="black", fg="white")
            self.name = tk.Entry(self)
            self.name.insert(0,data[1])
            lb2_s.place(x=10, y=40)
            self.name.place(x=110, y=40)

            lb2_des = tk.Label(self, text="Description - ", bg="black", fg="white")
            self.des = tk.Entry(self)
            self.des.insert(0,data[6])
            lb2_des.place(x=10, y=80)
            self.des.place(x=110, y=80)

            lb2_s = tk.Label(self, text="Room Types - ", bg="black", fg="white")
            lb2_s.place(x=10, y=160)
            lb2_s1 = tk.Label(self, text="Standard", bg="black", fg="white")
            lb2_s1.place(x=90, y=160)
            lb2_s2 = tk.Label(self, text="Deluxe", bg="black", fg="white")
            lb2_s2.place(x=160, y=160)
            lb2_s3 = tk.Label(self, text="Luxury", bg="black", fg="white")
            lb2_s3.place(x=230, y=160)
            self.lb2_s1 = tk.Entry(self, width='4')
            self.lb2_s1.place(x=100, y=200)

            self.lb2_s2 = tk.Entry(self, width='4')
            self.lb2_s2.place(x=170, y=200)
            self.lb2_s1.insert(0,data[2])
            self.lb2_s2.insert(0, data[3])

            self.lb2_s3 = tk.Entry(self, width='4')
            self.lb2_s3.place(x=240, y=200)
            self.lb2_s3.insert(0, data[4])

            lb2_price = tk.Label(self, text="Price - ", bg="black", fg="white")
            lb2_price.place(x=10, y=240)
            self.lb2_p1 = tk.Entry(self, width='4')
            self.lb2_p1.place(x=100, y=240)
            self.lb2_p1.insert(0, data[7])
            self.lb2_p2 = tk.Entry(self, width='4')
            self.lb2_p2.place(x=170, y=240)
            self.lb2_p2.insert(0, data[8])
            self.lb2_p3 = tk.Entry(self, width='4')
            self.lb2_p3.place(x=240, y=240)
            self.lb2_p3.insert(0, data[9])
            self.display = tk.Label(self, text='manas', bg="black")
            self.display2 = tk.Label(self, text='', bg="black")
            button_submit = tk.Button(self, text='Save', height=1, width=10, command=self.save)
            button_submit.place(x=160, y=290)
            button_back = tk.Button(self, text='Back', height=1, width=10, command=self.back )
            button_back.place(x=200, y=0)

    def save(self):
        try:
            cs = mydb.cursor()

            # drop clause
            statement = (
                        "UPDATE hotel_name SET hotelname='%s',standard_no='%s',deluxe_no='%s',luxury_no='%s',description='%s',sta_p='%s',dex_p='%s',lux_p='%s' WHERE id =%s" % (
                    self.name.get(), self.lb2_s1.get(), self.lb2_s2.get(), self.lb2_s3.get(), self.des.get(),
                    self.lb2_p1.get(), self.lb2_p2.get(), self.lb2_p3.get(), self.id))
            cs.execute(statement)
            # cs.execute(statement)
            mydb.commit()
            self.display2.config(bg="green", fg="white", text="Saved Success")
            # print('no')
            self.display2.place(x=20, y=1)
        except:
            self.display2.config(bg="green", fg="white", text="Not Success")
            # print('no')
            self.display2.place(x=20, y=1)

        # Disconnecting from the database
        # mydb.close()
    def back(self):
        self.destroy()
        a=admindash()



if __name__ == "__main__":
    app = edit_room()
    app.mainloop()