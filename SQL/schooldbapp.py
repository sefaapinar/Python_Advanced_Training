import mysql.connector

schooldb = mysql.connector.connect(
    
    host = "localhost",
    user= "root",
    password = "12345",
    port = "3308",
    database = "school"
)

mycurser = schooldb.cursor()

# mycurser.execute("Create Database school")

mycurser.execute("Show databases")



