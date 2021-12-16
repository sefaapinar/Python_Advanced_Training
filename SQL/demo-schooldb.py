
from typing import Counter
import mysql.connector
from datetime import datetime
from connection import connection

class Student:
    connection = connection
    mycursor = connection.cursor()

    def __init__(self, studentNo,name,surname,birthDate,gender):
        self.studentNo = studentNo,
        self.name = name,
        self.surname= surname,
        self.birthDate = birthDate,
        self.gender = gender
        
    def saveStudent(self):
        sql = "INSERT INTO  Student(studentNo,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
        value = (self.studentNo,self.name,self.surname,self.birthDate,self.gender)
        Student.mycursor.execute(sql,value)



ahmet = Student("102","Ahmet","Yılmaz",datetime(2000,7,8),"E")
ahmet.saveStudent()




ogrenciler = [
    ("101","Sefa","Pinar",datetime(2000,4,11),"E"),
    ("102","Mehmet","Dalkilic",datetime(2000,3,11),"E"),
    ("103","Ali","Bal",datetime(2000,6,7),"E"),
    ("104","Canan","Kiraz",datetime(2000,8,10),"K"),
    ("105","Erkan","Fidan",datetime(2000,9,12),"E")
]

Student.saveStudent(ogrenciler)

# try:
#     connection.commit()
#     print(F'{mycursor.rowcount} tane kayit eklendi')
# except mysql.connector.Error as err:
#     print('hata:', err)
# finally:
#     connection.close()
    
