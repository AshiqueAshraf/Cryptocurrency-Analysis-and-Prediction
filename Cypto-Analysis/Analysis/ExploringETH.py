import mysql.connector
from tkinter.ttk import *
from tkinter import *
from datetime import datetime
from tkcalendar import Calendar, DateEntry
from ExploringETHOpen import ExploringETHOpenClass
from ExploringETHHigh import ExploringETHHighClass
from ExploringETHLow import  ExploringETHLowClass
from ExploringETHClose import ExploringETHCloseClass
from ExploringETHVolume import ExploringETHVolumeClass

class ExploringETHClass:

    def __init__(self,top):
        self.top=top

        lab1 = ('Verdana', 11)
        bt_size = ('Verdana', 15)
        self.start_date = StringVar()
        self.end_date = StringVar()
        self.currency_status = StringVar()

        width = 600  # Width
        height = 650  # Height

        screen_width = top.winfo_screenwidth()  # Width of the screen
        screen_height = top.winfo_screenheight()  # Height of the screen

        # Calculate Starting X and Y coordinates for Window
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        top.geometry('%dx%d+%d+%d' % (width, height, x, y))

        top.geometry("600x400")

        top.title("EXPLORING ETH")

        top.configure(bg="light gray")

        userid = Label(top, text="ETH",font=("times new roman", 15, "bold"), bg="light gray").place(x=10, y=30)
        name = Label(top, text="To(end)", font=("times new roman", 15, "bold"),bg="light gray").place(x=10, y=180)
        dob =Label(top, text="From(start)", font=("times new roman", 15, "bold"),bg="light gray").place(x=10, y=130)
        designation = Label(top, text="Currency Status", font=("times new roman", 15, "bold"),bg="light gray").place(x=10, y=80)

        combo = Combobox(top,textvariabl=self.currency_status,font=lab1)
        combo['values'] = ("Open", "High", "Low", "Close", "Volume")
        combo.current(0)
        combo.place(x=250, y=80)

        login = Button(top, text="View Graph", font=bt_size, command=self.adduser).place(x=250, y=280)
        cancel = Button(top, text="Cancel", font=bt_size, command=top.destroy).place(x=420, y=280)

        cal = DateEntry(top, textvariable=self.start_date,width=14, font=('Georgia 17'), background="magenta3", foreground="white", bd=2).place(x=250, y=130)

        e5 = DateEntry(top, textvariable=self.end_date, width=14, font=('Georgia 17'), background="magenta3",foreground="white", bd=2).place(x=250, y=180)

        top.mainloop()

    def adduser(self):
        print('Button is pressed!')

        self.start_d = self.start_date.get()
        self.end_d = self.end_date.get()
        self.currency_s = self.currency_status.get()

        print("Currency Type:", self.currency_s)
        #dt_str = '27/10/20'

        start_obj = datetime.strptime(self.start_d, '%m/%d/%y').date()
        end_obj = datetime.strptime(self.end_d, '%m/%d/%y').date()

        print("Sart Date:", start_obj)
        print("End date:", end_obj)

        if self.currency_s=="Open":
            ob=ExploringETHOpenClass()
            print("Inside if...")
            ob.check()
            ob.eth_open_price(start_obj,end_obj)
        elif  self.currency_s=="High":
            ob = ExploringETHHighClass()
            ob.eth_high_price(start_obj, end_obj)
        elif  self.currency_s=="Low":
            ob = ExploringETHLowClass()
            ob.eth_low_price(start_obj, end_obj)
        elif  self.currency_s=="Close":
            ob = ExploringETHCloseClass()
            ob.eth_close_price(start_obj, end_obj)
        elif  self.currency_s=="Volume":
            ob = ExploringETHVolumeClass()
            ob.eth_volume_price(start_obj, end_obj)
        else:
            print("Incorrect entry")


#cp=Tk()
#ob=ExploringETHClass(cp)






