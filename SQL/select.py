import mysql.connector

def getProducts():
    connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "12345",
    database = "node-app",
    port = "3308"
)
    cursor = connection.cursor()
    cursor.execute('Selecting * from Product')

    result = cursor.fetchall()

    print(result)

getProducts()