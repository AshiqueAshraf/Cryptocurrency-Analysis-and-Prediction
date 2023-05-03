from tkinter.ttk import *
from tkinter import *
from dbconnection import myconnection
import mysql.connector

import foo
import os
print("My Path..",os.getcwd())
pr_path = os.getcwd()
n=pr_path.rfind("\\")
root_path=pr_path[:n]

#LtColonelProfileViewClass

class UserProfileViewClass:
    def __init__(self, top):
        self.top = top
        large_font = ('Verdana', 15)
        large_font2 = ('Verdana', 15)
        large_font3 = ('Verdana', 15)
        lab1 = ('Verdana', 15)
        lab2 = ('Verdana', 15)

        large_font = ('Verdana', 15)
        large_font2 = ('Verdana', 15)
        large_font3 = ('Verdana', 15)
        lab1 = ('Verdana', 15)
        lab2 = ('Verdana', 15)

        bt_size = ('Verdana', 15)

        # top = Tk()

        self.uname = StringVar()
        self.upass = StringVar()
        self.gender= StringVar()
        self.dob = StringVar()
        self.address = StringVar()
        self.city = StringVar()
        self.pin = StringVar()
        self.designation= StringVar()

        # top.state("zoomed")
        """windowWidth = top.winfo_reqwidth()
        windowHeight = top.winfo_reqheight()
        print("Width", windowWidth, "Height", windowHeight)

        positionRight = int(top.winfo_screenwidth() / 3 - windowWidth / 2)
        positionDown = int(top.winfo_screenheight() / 3 - windowHeight / 2)

        # Positions the window in the center of the page.
        top.geometry("+{}+{}".format(positionRight, positionDown))
        top.geometry("+{}+{}".format(600, 250))"""

        width = 440  # Width
        height = 500  # Height

        screen_width = top.winfo_screenwidth()  # Width of the screen
        screen_height = top.winfo_screenheight()  # Height of the screen

        # Calculate Starting X and Y coordinates for Window
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        top.geometry('%dx%d+%d+%d' % (width, height, x, y))
        #top.geometry("440x500")

        top.title("User Profile View")

        userid = Label(top, text="Enter ID", font=lab1).place(x=10, y=30)
        password = Label(top, text="Date Of Birth", font=lab2).place(x=10, y=80)
        name = Label(top, text="Name", font=lab2).place(x=10, y=130)
        gender = Label(top, text="Gender", font=lab2).place(x=10, y=180)

        designation = Label(top, text="Designation",  font=lab2).place(x=10, y=230)

        address = Label(top, text="Address", font=lab2).place(x=10, y=280)
        city = Label(top, text="City", font=lab2).place(x=10, y=330)
        pin = Label(top, text="Pin", font=lab2).place(x=10, y=380)
        #login = Button(top, text="Remove", font=bt_size ).place(x=300, y=430)
        cancel = Button(top, text="Cancel", font=bt_size, command=top.destroy).place(x=300, y=430)
        #e8 = Button(top, text="search", font=bt_size).place(x=410, y=30)

        e1 = Entry(top, width=15, textvariable=self.uname, font=large_font2).place(x=200, y=30)
        e2 = Entry(top, width=15, textvariable=self.upass, font=large_font2).place(x=200, y=80)
        e3 = Entry(top, width=15, textvariable=self.dob, font=large_font2).place(x=200, y=130)
        e9 = Entry(top, width=15, textvariable=self.designation, font=large_font2).place(x=200, y=230)

        e22 = Entry(top, width=15, textvariable=self.gender, font=large_font2).place(x=200, y=180)

        e5 = Entry(top, width=15,textvariable=self.address, font=large_font2).place(x=200, y=280)
        e6 = Entry(top, width=15,textvariable=self.city, font=large_font2).place(x=200, y=330)
        e7 = Entry(top, width=15, textvariable=self.pin,font=large_font2).place(x=200, y=380)

        mydb=myconnection()
        mycursor = mydb.cursor()
        #curid = "100"
        curid = foo.USER_NAME_ID
        print("User Name........:", curid)
        sql = "select * from adduser where userid=%s"
        val = (curid,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        print("success...")
        print("Result...record:",myresult)
        for record in myresult:
            print("Data....", record)
            self.uname.set(record[0])
            self.upass.set(record[2])
            self.dob.set(record[1])
            #self.city.set(record[7])
            self.gender.set(record[4])
            self.designation.set(record[5])
            self.address.set(record[6])
            self.city.set(record[7])
            self.pin.set(record[8])
        top.mainloop()
#top=Tk()
#cp= LtColonelProfileViewClass(top)
