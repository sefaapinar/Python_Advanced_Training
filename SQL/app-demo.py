import mysql.connector
from datetime import datetime
from connection import connection

class Student:
    connection = connection
    mycursor = connection.cursor

    def __init__(self,studentNo, name,surname,birthdate,gender) -> None:


    

    @staticmethod    
    def saveStudents(students):
        sql = "INSERT INTO Student(studentNo,name,surname,birthdate,gender)"
        values = students
        Student.mycursor.executemany(sql,values)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt eklendi')
        except mysql.connector.Error as err:
            print('hata',err)
        finally:
            Student.connection.close()
    @staticmethod
    def StudentInfo():
        sql = ""
