from tkinter import *
from tkinter import ttk
import mysql.connector
from dbconnection import myconnection

#ListAll
class ListAllUsersClass:
    def __init__(self, top):

        width = 1000  # Width
        height = 350  # Height

        screen_width = top.winfo_screenwidth()  # Width of the screen
        screen_height = top.winfo_screenheight()  # Height of the screen

        # Calculate Starting X and Y coordinates for Window
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        top.geometry('%dx%d+%d+%d' % (width, height, x, y))
        top.title("List All Users")
        """mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="crypto"
        )"""
        mydb=myconnection()
        mycursor = mydb.cursor()
        sql = "select * from adduser"
        mycursor.execute(sql)
        records = mycursor.fetchall()


        # Set the size of the tkinter window
        #top.geometry("1000x350")

        # Create an object of Style widget
        style = ttk.Style()
        style.theme_use('clam')

        # Add a Treeview widget
        tree = ttk.Treeview(top, column=("USER ID", "NAME", "DOB","QUALIFICATION","GENDER","DESIGNATION","ADDRESS","CITY","PIN"), show='headings', height=5)
        tree.column("# 1", anchor=CENTER, width=100)
        tree.heading("#1", text="USER ID")

        tree.column("# 2", anchor=CENTER, width=100)
        tree.heading("# 2", text="NAME")

        tree.column("# 3", anchor=CENTER, width=100)
        tree.heading("# 3", text="DOB")

        tree.column("# 4", anchor=CENTER, width=100)
        tree.heading("# 4", text="QUALIFICATION")

        tree.column("# 5", anchor=CENTER, width=100)
        tree.heading("# 5", text="GENDER")

        tree.column("# 6", anchor=CENTER, width=100)
        tree.heading("# 6", text="DESIGNATION")

        tree.column("# 7", anchor=CENTER, width=100)
        tree.heading("# 7", text="ADDRESS")

        tree.column("# 8", anchor=CENTER, width=100)
        tree.heading("# 8", text="CITY")

        tree.column("# 9", anchor=CENTER, width=100)
        tree.heading("# 9", text="PIN")

        for row in records:
            # Insert the data in Treeview widget
            tree.insert('', 'end', text="1", values=(row[0], row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8]))

        """tree.insert('', 'end', text="1", values=('Ankush', 'Mathur', '17702'))
        tree.insert('', 'end', text="1", values=('Manisha', 'Joshi', '17703'))
        tree.insert('', 'end', text="1", values=('Shivam', 'Mehrotra', '17704'))"""

        tree.pack()

        top.mainloop()

#top= Tk()
#cp=ListAllUsersClass(top)