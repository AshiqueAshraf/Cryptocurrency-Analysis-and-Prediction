import mysql.connector
from tkinter.ttk import *
from tkinter import *
from datetime import datetime
from tkcalendar import DateEntry
from PredictingBTCOpen import PredictingBTCOpenClass
from PredictingBTCHigh import PredictingBTCHighClass
from PredictingBTCLow import  PredictingBTCLowClass
from PredictingBTCClose import PredictingBTCCloseClass
from PredictingBTCVolume import PredictingBTCVolumeClass

class PredictingBTCClass:

    def __init__(self,top):
        self.top=top
        lab1 = ('Verdana', 11)
        bt_size = ('Verdana', 15)
        self.predict_date = StringVar()
        #self.end_date = StringVar()
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

        top.title("Predicting BTC")

        top.configure(bg="light gray")

        userid = Label(top, text="BTC",font=("times new roman", 15, "bold"), bg="light gray").place(x=10, y=30)
        #name = Label(top, text="To(end)", font=("times new roman", 15, "bold"),bg="light gray").place(x=10, y=180)
        dob =Label(top, text="Date To Predict", font=("times new roman", 15, "bold"),bg="light gray").place(x=10, y=150)
        designation = Label(top, text="Currency Status", font=("times new roman", 15, "bold"),bg="light gray").place(x=10, y=80)

        combo = Combobox(top,textvariabl=self.currency_status,font=lab1)
        combo['values'] = ("Open", "High", "Low", "Close")
        combo.current(0)
        combo.place(x=250, y=80)

        login = Button(top, text="Predict", font=bt_size, command=self.predict).place(x=250, y=280)
        cancel = Button(top, text="Cancel", font=bt_size, command=top.destroy).place(x=420, y=280)

        cal = DateEntry(top, textvariable=self.predict_date,width=14, font=('Georgia 17'), background="magenta3", foreground="white", bd=2).place(x=250, y=150)

        #e5 = DateEntry(top, textvariable=self.end_date, width=14, font=('Georgia 17'), background="magenta3",foreground="white", bd=2).place(x=250, y=180)

        top.mainloop()

    def predict(self):
        print('Button is pressed!')

        self.predict_d = self.predict_date.get()
        #self.end_d = self.end_date.get()
        self.currency_s = self.currency_status.get()

        print("Currency Type:", self.currency_s)
        #dt_str = '27/10/20'

        print("Predict Date.........:",self.predict_d)
        #print("End Date...:",self.end_d)
        predict_obj = datetime.strptime(self.predict_d, '%m/%d/%y').date()
        #end_obj = datetime.strptime(self.end_d, '%m/%d/%y').date()

        print("Pdict Date Final:", predict_obj)
        #print("End date:", end_obj)
        print("I am here...")
        str_date=str(predict_obj)
        print("Splited...")
        #print(str_date.split("-"))

        lis = str_date.split("-")
        res = [int(i) for i in lis]
        print("Modified list is: ", res)
        res1=[res]
        print("Final Date list: ", res1)

        #ob=PredictingBTCOpenClass()
        #ob.predict_btc_open_price(res1)
        if self.currency_s=="Open":
            print("Inside if...")
            ob = PredictingBTCOpenClass()
            ob.predict_btc_open_price(res1)
        elif self.currency_s == "High":
            ob = PredictingBTCHighClass()
            ob.predict_btc_high_price(res1)
        elif self.currency_s == "Low":
            ob = PredictingBTCLowClass()
            ob.predict_btc_low_price(res1)
        elif self.currency_s == "Close":
            ob = PredictingBTCCloseClass()
            ob.predict_btc_close_price(res1)
        elif self.currency_s == "Volume":
            ob = PredictingBTCVolumeClass()
            ob.predict_btc_volume_price(res1)
        else:
            print("No match")
#cp=Tk()
#ob=PredictingBTCClass(cp)






