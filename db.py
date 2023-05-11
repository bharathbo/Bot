import mysql.connector
from  telegram.ext import Updater


def database():
    
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bot"
    )
    mycursor = mydb.cursor()
    return mydb, mycursor


def update():
    updater = Updater(token='token', use_context=True)
    return updater 

    

