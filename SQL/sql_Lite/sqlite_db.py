import sqlite3
from sqlite3.dbapi2 import connect

connection = sqlite3.connect("chinook.db")

cursor = connection.cursor()

cursor.execute("Select * from customers")
result = cursor.fetchall()


for i in result:
    print(i)

connection.close()