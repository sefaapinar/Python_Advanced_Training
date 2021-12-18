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

    #sql = "select * from products"
    #sql = "select * from categories"
    #sql = "select * from produts inner join Categories on Categories.id=Products.Categoryid"
    #sql = "Select Products.name,Products.price,Categories.name From Products inner join Categories on Categories.id=Products.Categoryid "
    #sql = "Select Products.name,Products.price,Categories.name From Products inner join Categories on Categories.id=Products.Categoryid where categories.name='Telefon'"
    #sql = "Select Products.name,Products.price,Categories.name From Products inner join Categories on Categories.id=Products.Categoryid where products.name='Xiaomi'"
    sql = "Select p.name,p.price,c.name From Products as  p inner join Categories on c.id=p.Categoryid "





    cursor.execute(sql)

    try:
        result = cursor.fetchall()
        for product in result:
           print(product)
    except mysql.connector.Error as err:
        print('hata:',err)
    finally:
        connection.close()

getProducts()