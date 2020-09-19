import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
from db import *
from admin_dashboard import *

class addroom(tk.Tk):
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.file=''
        self.title("Add Hotel")
        self.geometry("300x200")
        self.config(background="black", pady=10)
        lbs = tk.Label(self, text="Add Hotel", bg="black", fg="white", font=20)
        lbs.place(x=110, y=15)

        lb2_s = tk.Label(self, text="Hotel Name - ", bg="black", fg="white")
        self.name = tk.Entry(self)
        lb2_s.place(x=10, y=40)
        self.name.place(x=110, y=40)

        lb2_des = tk.Label(self, text="Description - ", bg="black", fg="white")
        self.des = tk.Entry(self)
        lb2_des.place(x=10, y=80)
        self.des.place(x=110, y=80)
        lb2_img = tk.Label(self, text="Image - ", bg="black", fg="white")
        button = tk.Button(self, text='Open', command=self.UploadAction)
        button.place(x=110,y=120)
        lb2_img.place(x=10,y=120)

        lb2_s = tk.Label(self, text="Room Types - ", bg="black", fg="white")
        lb2_s.place(x=10, y=160)
        lb2_s1 = tk.Label(self, text="Standard", bg="black", fg="white")
        lb2_s1.place(x=90, y=160)
        lb2_s2 = tk.Label(self, text="Deluxe", bg="black", fg="white")
        lb2_s2.place(x=160, y=160)
        lb2_s3 = tk.Label(self, text="Luxury", bg="black", fg="white")
        lb2_s3.place(x=230, y=160)
        self.lb2_s1 = tk.Entry(self,width='4')
        self.lb2_s1.place(x=100, y=200)

        self.lb2_s2 = tk.Entry(self, width='4')
        self.lb2_s2.place(x=170, y=200)

        self.lb2_s3 = tk.Entry(self, width='4')
        self.lb2_s3.place(x=240, y=200)

        lb2_price = tk.Label(self, text="Price - ", bg="black", fg="white")
        lb2_price.place(x=10, y=240)
        self.lb2_p1 = tk.Entry(self, width='4')
        self.lb2_p1.place(x=100, y=240)
        self.lb2_p2 = tk.Entry(self, width='4')
        self.lb2_p2.place(x=170, y=240)
        self.lb2_p3 = tk.Entry(self, width='4')
        self.lb2_p3.place(x=240, y=240)
        self.display = tk.Label(self,text='manas', bg="black")
        self.display2 = tk.Label(self, text='', bg="black")
        button_submit = tk.Button(self, text='Save',height=1,width=10, command=self.save)
        button_submit.place(x=160, y=290)
        button_back = tk.Button(self, text='Back', height=1, width=10, command=self.back)
        button_back.place(x=200, y=0)


    def UploadAction(self,event=None):

        filename = filedialog.askopenfilename()
        if (filename.endswith('.jpeg'))or(filename.endswith('.jpg')):
            self.display.destroy()
            # x = openfn()
            self.file=filename
            img = Image.open(filename)
            img = img.resize((250, 250), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            panel = tk.Label(self, image=img,height=70,width=70)
            panel.image = img
            panel.place(x=240,y=40)
            print('Selected:', filename)
        else:
            self.display.config(bg="green", fg="white", text="please select image only")
            # print('no')
            self.display.place(x=240, y=80)

    def save(self):
        # print(self.lb2_s1.get(),self.lb2_s1.get(),self.lb2_s3.get(),self.name.get(),self.file)
        if ((len(self.name.get()) == 0) and (len(self.lb2_s3.get()) == 0) and (len(self.lb2_s2.get()) == 0) and (
                len(self.lb2_s1.get()) == 0) and (len(self.file) == 0) and (len(self.des.get()) == 0)):
            print('error')
            self.display2.config(bg="red", fg="white", text="please fill all the details")
            self.display2.place(x=20, y=1)
        else:
            try:
                mycursor = mydb.cursor()

                sql = "INSERT INTO hotel_name (hotelname,luxury_no,deluxe_no,standard_no, image,description,sta_p,dex_p,lux_p) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s)"
                val = (
                self.name.get(), self.lb2_s3.get(), self.lb2_s2.get(), self.lb2_s1.get(), self.file, self.des.get(),self.lb2_p1.get(),self.lb2_p2.get(),self.lb2_p3.get())
                mycursor.execute(sql, val)

                mydb.commit()

                print(mycursor.rowcount, "record inserted.")
                self.display2.config(bg="green", fg="white", text="Saved Success")
                # print('no')
                self.display2.place(x=20, y=1)
            except:

                print(len(self.file()))
    def back(self):
        self.destroy()
        a=admindash()



if __name__ == "__main__":
    app = addroom()
    app.mainloop()