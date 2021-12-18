# import mysql.connector
# from datetime import datetime


# from connection import connection

# # class Student:
# #     connection = connection
# #     mycursor = connection.cursor

# #     def __init__(self,studentNo, name,surname,birthdate,gender) -> None:


    

#     # # @staticmethod    
#     # def saveStudents(students):
#     #     sql = "INSERT INTO Student(studentNo,name,surname,birthdate,gender)"
#     #     values = students
#     #     Student.mycursor.executemany(sql,values)

#     #     try:
#     #         Student.connection.commit()
#     #         print(f'{Student.mycursor.rowcount} tane kayıt eklendi')
#     #     except mysql.connector.Error as err:
#     #         print('hata',err)
#     #     finally:
#     #         Student.connection.close()
#     # @staticmethod
#     # def StudentInfo():
#     #     #sql = "select studentno,name,surname,from, student"
#     #     # sql = "select name,surname, from student where gender = 'k' "
#     #     # sql = "select * from student where YEAR(birthdate) = 2003"
#     #     # sql = "select * from student where name like '%an%' or surname like '%an%'"
#     #     # sql = "select Count(*) from student where gender = 'E'"
#     #     sql = " select * from student where  gender = 'k ' order by name, surname"



#     #     Student.mycursor.execute(sql)

#     #     try:
#     #         resuts = Student.mycursor.fetchall()
            
#     #         for result in resuts:
#     #             print(f'{result[0]} {result[1]}')
#     #     except mysql.connector.Error as err:
#     #         print('hata',err)
#     #     finally:
#     #         Student.connection.close()

# def updateProduct():
   
#     connection = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "12345",
#     database = "node-app",
#     port = "3308"
# )
#     cursor = connection.cursor()

#     sql = "Update products Set name='Samsung S10',price = 5000 where id=2"


#     cursor.execute(sql)

#     try:
#         connection.commit()
#         print(f'{cursor.rowcount} tane kayıt güncellendi.')
#     except mysql.connector.Error as err:
#         print('hata:', err)
#     finally:
#         connection.close()
#         print('Database bağlantısı kapandı.')

# # updateProduct()


# def deleteProduct():
     
#     connection = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "12345",
#     database = "node-app",
#     port = "3308"
# )
#     cursor = connection.cursor()

#     sql = "Delete from products where id = 2"


#     cursor.execute(sql)

#     try:
#         connection.commit()
#         print(f'{cursor.rowcount} tane kayıt silindi.')
#     except mysql.connector.Error as err:
#         print('hata:', err)
#     finally:
#         connection.close()
#         print('Database bağlantısı kapandı.')

# deleteProduct()


# @staticmethod
# def getStundetById(id):
#         sql = "Select * from student where id=%s"
#         value = (id,)

#         Student.mycursor.exeute(sql,value)

#         try:
#             return Student.mycursor.fetchone()

#         except mysql.connector.Error as err:
#             print('Error', err)
#         finally:
#             Student.connection.close()


# def updateStudent(self):
#         sql = "update student set studenno=%s,name =%s,birhtdate=%s,gender=%s"
#         values = (self.studentNumber, self.name, self.birthdate, self.gender, self.id,self.surname)

# obj = Student.getStudentById(7)
# print(obj)