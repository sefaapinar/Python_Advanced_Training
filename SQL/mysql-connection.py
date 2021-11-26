import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",  # 192.168.23.21
    user = "root",
    password ="12345",
    port="3308",
    database="node-app"
)
  
mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase") # database olusturma islemi

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))") 



print(mydb)
