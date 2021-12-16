import mysql.connector
from mysql.connector import connection


def insertProduct(name,price,imageUrl,description):
    connection = mysql.connector.connect(
    
        host = "localhost",
        user= "root",
        password = "12345",
        port = "3308",
        database = "node-app"
        
)

    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,imageURL,description) VALUES (%s,%s,%s,%s)"
    values = (name,price,imageUrl,description)
    cursor.execute(sql,values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayıt eklendi')
        print(f'son eklenen kaydın id: {cursor.lastrowid}')

    except mysql.connector.Error as err:
        print('hata:',err)

    finally:
        connection.close()
        print('Database bağlantısı kapandı')

list = []
while True:


    name = input('Ürün Adı:')
    price = input('Ürün fiyatını giriniz: ')
    imageUrl = input('Ürün resim adı: ')
    description = input('Ürün açıklamasını giriniz: ')
    list .append((name,price,imageUrl,description))
    result = input('Devam etmek istiyor musunuz = (e/h)')
    if result == 'h':
        print('Kayitlariniz veri tabanina aktarılıyor')
        print(list)
        # kayıt işlemi

insertProduct(name,price,imageUrl,description)

