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
    updater = Updater(token='6267642713:AAH9C0BKY7C56-jrBw6fPVssrl_ElDhM5kU', use_context=True)
    return updater 

    

