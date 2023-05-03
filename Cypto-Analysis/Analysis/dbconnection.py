import mysql.connector
def myconnection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="crypto"
    )
    return mydb