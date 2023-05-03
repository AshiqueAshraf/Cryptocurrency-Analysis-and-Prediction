#!/usr/bin/env python
import mysql.connector
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from AdminProfile import  AdminProfileClass
from addnewuser import AddNewUserClass
from myprofile import MyprofileClass
from AdminPasswordChange import AdminPasswordChangeClass
from RemoveUser import RemoveUserClass
from ListAllUsers import ListAllUsersClass
from AdminIDBasedSearch import  AdminIDBasedSearchClass
from UserPasswordChange import *
from UserProfileView import *
from dbconnection import myconnection
from ExploringBTC import ExploringBTCClass
from PredictingBTC import PredictingBTCClass
from PredictingETH import PredictingETHClass
from PredictingDOGE import PredictingDOGEClass
from ExploringETH import ExploringETHClass
from ExploringDOGE import ExploringDOGEClass
import random
import string
import requests
import json
import foo
import os
print("My Path..",os.getcwd())
pr_path = os.getcwd()
n=pr_path.rfind("\\")
root_path=pr_path[:n]

#print("im_path......:",im_path)

top = Tk()

uname = StringVar()
upass = StringVar()
USER_TYPE=StringVar()
#--------------------------------------------------------------

def userpasschange():
    print("clicked")
    window = Toplevel()
    app = AdminPasswordChangeClass(window)

def userview():
    print("clicked")
    window = Toplevel()
    app = UserProfileViewClass(window)

def btcreport():
    print("clicked")
    window = Toplevel()
    ob=ExploringBTCClass(window)
def ethreport():
    print("clicked")
    window = Toplevel()
    ob=ExploringETHClass(window)
def dogereport():
    print("clicked")
    window = Toplevel()
    ob=ExploringDOGEClass(window)
def btcpredict():
    print("clicked")
    window = Toplevel()
    ob=PredictingBTCClass(window)
def ethpredict():
    print("clicked")
    window = Toplevel()
    ob=PredictingETHClass(window)
def dogepredict():
    print("clicked")
    window = Toplevel()
    ob=PredictingDOGEClass(window)
def userhome():
    master = Toplevel()
    master.title("User Home")
    master.state("zoomed")
    im_path1 = root_path + '\\IMAGES\\new.png'
    print("new path:", im_path1)
    img = ImageTk.PhotoImage(file=im_path1)
    w, h = img.width(), img.height()
    canvas = Canvas(master, width=w, height=h, bg='blue', highlightthickness=0)
    canvas.pack(expand=YES, fill=BOTH)
    canvas.create_image(0, 0, image=img, anchor=NW)

    menubar = Menu(master)
    file = Menu(menubar, tearoff=0)

    file.add_command(label="View Profile", command=userview)
    file.add_command(label="Change password", command=userpasschange)

    file.add_separator()

    file.add_command(label="Logout", command=master.destroy)

    menubar.add_cascade(label="My Profile", menu=file)

    btc = Menu(menubar, tearoff=0)

    btc.add_command(label="BTC Report ", command=btcreport)
    btc.add_command(label="ETH Report ", command=ethreport)
    btc.add_command(label="DOGE Report ", command=dogereport)

    #btc.add_command(label="View Information Report", command=ltcolonelreportview)

    menubar.add_cascade(label="Crypto Exploring", menu=btc)
    prediction = Menu(menubar, tearoff=0)
    prediction.add_command(label="BTC Prediction", command=btcpredict)
    prediction.add_command(label="ETH Prediction", command=ethpredict)
    prediction.add_command(label="DOGE Prediction", command=dogepredict)

    menubar.add_cascade(label="Crypto Prediction", menu=prediction)

    master.config(menu=menubar)
    master.mainloop()
#------------------------------------------------------------------------------------
def adminprofile():
        print("clicked")
        window = Toplevel()
        app = AdminProfileClass(window)

def showchangepassword():
    print("clicked")
    window = Toplevel()
    app = AdminPasswordChangeClass(window)

def addnewuser():
    print("clicked")
    window =  Toplevel()
    app = AddNewUserClass(window)
def showremoveuser():
    print("clicked")
    window = Toplevel()
    app = RemoveUserClass(window)
def idbased():
    print("clicked")
    window = Toplevel()
    app = AdminIDBasedSearchClass(window)
def rankbased():
    print("clicked")
    window = Toplevel()
    #app = RankBasedSearchClass(window)
def listallusers():
    print("clicked")
    window = Toplevel()
    app = ListAllUsersClass(window)

def adminhome():
    master1 = Toplevel()
    master1.title("Admin Home")
    master1.state("zoomed")
    im_path8 = root_path + '\\IMAGES\\new.png'
    print("new path:",im_path8)
    img = ImageTk.PhotoImage(file=im_path8)
    w, h = img.width(), img.height()
    canvas = Canvas(master1, width=w, height=h, bg='blue', highlightthickness=0)
    canvas.pack(expand=YES, fill=BOTH)
    canvas.create_image(0, 0, image=img, anchor=NW)

    menubar = Menu(master1)
    file = Menu(menubar, tearoff=0)
    #file.add_command(label="my profile")
    file.add_command(label="My Profile", command=adminprofile)

    #file.add_command(label="New Officer Appointment")
    file.add_command(label="Add New User", command=addnewuser)

    #file.add_command(label="Remove Officer")
    file.add_command(label="Remove User", command=showremoveuser)

    #file.add_command(label="Change Password")
    file.add_command(label="Change Password", command=showchangepassword)

    file.add_separator()
    file.add_command(label="Logout", command=master1.destroy)

    menubar.add_cascade(label="User Activites", menu=file)
    edit = Menu(menubar, tearoff=0)
    #edit.add_command(label="IDBased")
    edit.add_command(label="IDBased List", command=idbased)

    #edit.add_command(label="Rank Based")
    #edit.add_command(label="Rank Based", command=rankbased)

    edit.add_separator()

    #edit.add_command(label="Select All Officers")
    edit.add_command(label="List All Users", command=listallusers)

    menubar.add_cascade(label="LogReport", menu=edit)
    help = Menu(menubar, tearoff=0)
    help.add_command(label="About")
    menubar.add_cascade(label="Help", menu=help)

    master1.config(menu=menubar)
    print("inside admin...")
    master1.mainloop()

def getuserid():
    return USER_ID

def chooseaction():
    global USER_ID
    u_name = uname.get()
    u_pass = upass.get()
    print("Username:", u_name)
    print("Password:", u_pass)

    USER_ID=u_name



    """mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="crypto"
    )"""
    mydb=myconnection()
    mycursor = mydb.cursor()

    #mycursor = createcursor()
    #USERID=u_name
    sql = "select * from login where userid=%s and password=%s"
    adr = (u_name, u_pass)
    mycursor.execute(sql, adr)
    records = mycursor.fetchall()
    print("done")
    USER_TYPE = ""
    for row in records:
        USER_TYPE = row[2]
        print(USER_TYPE)
    #print("my user name is:", USER_TYPE)

    if USER_TYPE != "":
        top.withdraw()
        if USER_TYPE=="admin":
            print("admin here")
            foo.USER_NAME_ID = u_name
            #print("Current user...:", foo.USER_NAME_ID)
            adminhome()
        elif USER_TYPE=="user":
            print("user here")
            foo.USER_NAME_ID = u_name
            print("Current user...:", foo.USER_NAME_ID)
            userhome()
    else:
        messagebox.showinfo("Alert","No Such User...")


def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)


def onclick():

    global USER_ID
    u_name = uname.get()
    u_pass = upass.get()
    print("Username:", u_name)
    print("Password:", u_pass)
    USER_ID=u_name

    foo.USER_NAME_ID = u_name

    """mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="crypto"
    )"""
    mydb = myconnection()
    mycursor = mydb.cursor()

    #mycursor = createcursor()
    #USERID=u_name

    sql = "select userid,password from login where userid=%s"
    adr=(u_name,)
    mycursor.execute(sql,adr)
    records = mycursor.fetchall()


    status=False
    USER_TYPE = ""
    PASS=""
    MY_USER=""
    for row in records:
        #print("ROW..",row)
        print("user......",row[0])
        print("password...",row[1])
        #USER_TYPE = row[0]
        #print(U)
        status=True
        if status==True:
            MY_USER=row[0]
            PASS=row[1]
            break
    if status==False:
        messagebox.showinfo("Alert", "no such user...")
    elif status==True:
        print("user......",MY_USER)
        print("PASSSSSSSSSSSSSSSSSS:",PASS)

        p=MY_USER[len(MY_USER)-2:]
        messagebox.showinfo("Alert","An OTP has send to ********"+p)

        OTP=randomString()
        print(OTP)
#------------------------------------------------------------------------------------------------
        CHECK_ID=uname.get()
        print("user id",CHECK_ID)
        """mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="army"
        )"""
        mydb = myconnection()
        mycursor = mydb.cursor()

        # mycursor = createcursor()
        # USERID=u_name

        sql = "update login set password=%s where userid=%s"
        val = (OTP, CHECK_ID)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")

        #response = sendPostRequest(URL, 'APQ29I7R7SS93Z42RGI8MTLNUB9FNYV8', '26TE4BLBWN8SS7LA', 'stage',CHECK_ID,'9061259158','YOUR ONE TIME PASSWORD: ' +OTP)
        #response = sendPostRequest(URL, 'APQ29I7R7SS93Z42RGI8MTLNUB9FNYV8', '26TE4BLBWN8SS7LA', 'stage', "7510625756",'9061259158', PASS)
    window = Toplevel()
    #app = OtpPasswordClass(window)

    # print("my user name is:", USER_TYPE)

def randomString(stringLength=6):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase


    return ''.join(random.choice(letters) for i in range(stringLength))

def validate(e):
    #self.e=e

    if (e.isdigit()):
        return True
    else:
        return False

def loginfunction():
    large_font = ('Verdana', 15)
    large_font2 = ('Verdana', 15)
    lab1 = ('Verdana', 15)
    lab2 = ('Verdana', 15)
    bt_size = ('Verdana', 15)

    im_path1 = root_path + '\\IMAGES\\cr.png'
    img = ImageTk.PhotoImage(file=im_path1)
    w, h = img.width(), img.height()
    canvas = Canvas(top, width=w, height=h, bg='white', highlightthickness=0)
    canvas.pack(expand=YES, fill=BOTH)
    canvas.create_image(0, 0, image=img, anchor=NW)
    im_path2 = root_path + '\\IMAGES\\man_user.png'
    #user_icon = ImageTk.PhotoImage(file="F:\\DATASCIENCE\\Ashique_Project\\CryptoAnalysis\\IMAGES\\man_user.png")
    user_icon = ImageTk.PhotoImage(file=im_path2)
    im_path3 = root_path + '\\IMAGES\\pas.png'
    #pass_icon = ImageTk.PhotoImage(file="F:\\DATASCIENCE\\Ashique_Project\\CryptoAnalysis\\IMAGES\\pas.png")
    pass_icon = ImageTk.PhotoImage(file=im_path3)
    im_path4 = root_path + '\\IMAGES\\logo.png'
    #logo_icon = ImageTk.PhotoImage(file="F:\\DATASCIENCE\\Ashique_Project\\CryptoAnalysis\\IMAGES\\logo.png")
    logo_icon = ImageTk.PhotoImage(file=im_path4)
    # logo_icon= PhotoImage(file="password.png")

    Login_Frame = Frame(top, bg="White")
    Login_Frame.place(x=560, y=380)
    logo_lbl = Label(Login_Frame, image=logo_icon).grid(row=0, column=0, pady=20)


    top.title("Login")

    top.configure(bg="light gray")
    top.state("zoomed")

    email = Label(Login_Frame, text="User ID", font=lab1, bg="white", fg="black", image=user_icon, compound=LEFT).grid(row=1, column=0, padx=20, pady=10)

    password = Label(Login_Frame, text="Password", font=lab2, bg="white", fg="black", image=pass_icon,compound=LEFT).grid(row=2, column=0, padx=20, pady=10)


    cancel = Button(top, text="Cancel", font=bt_size,width=20,relief=RIDGE,bg="light gray",command=top.destroy).place(x=1200, y=570)
    #logout = Button(top, text="Sign-in", font=bt_size, command = loadhomes).place(x=235, y=170)
    logout = Button(top, text="Sign-in", font=bt_size, width=20,relief=RIDGE,command=chooseaction).place(x=1200, y=470)
    psswd = Button(top, text="Forgot Password?", font=bt_size, bg="light gray",width=20,relief=RIDGE, fg="black",command=onclick).place(x=1200,y=670)
    val = top.register(validate)

    #Entry(Login_Frame, textvariable=uname, width=15, font=large_font, validate="key", validatecommand=(val, '%S')).grid(row=1,column=1,padx=20,pady=10)
    Entry(Login_Frame, textvariable=uname, width=15, font=large_font).grid(row=1, column=1, padx=20, pady=10)
    # e2 = Entry(master,  width=15,font=large_font).place(x = 130, y = 30)
    # text = e2.get()
    e3 = Entry(Login_Frame, textvariable=upass, show="*", width=15, font=large_font2).grid(row=2,column=1,padx=20,pady=10)

    # e3 = Entry(master, width=15,font=large_font2).place(x = 130, y = 100)
    top.mainloop()

loginfunction()




