#base class yani temel sınıf ve 
#parent class 


#child class  bu classlar temel sınıflardan oluşur.

from _typeshed import Self


class Person:
    def __init__(self,name,surname,age) -> None:
        self.name = name
        self.surname = surname
        self.age = age
        print("Person Nesnesi Türetildi.")

# class intro(self):
#     print(self.name,self.surname,self.age)

class Student(Person):
    def __init__(self,name,surname,age,number):
        Person.__init__(self,name,surname,age)
        self.number = number
        print("Student nesnesi üretildi")
       
    
 

class Teacher(Person):
     def __init__(self, name, surname, age,branch) -> None:
         Person.__init__(name, surname, age)
         self.branch = branch
         print("Teacher Nesnesi Üretildi.")
    


# t1 = Teacher()
p1 = Person("Sefa","Pınar",40)
# s1 = Student()

print(p1.name,p1.surname,p1.age)