import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",  # 192.168.23.21
    user = "root",
    password ="12345",
    port="3308",
    database="node-app"
)
  
