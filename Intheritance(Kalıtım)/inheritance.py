#base class yani temel sınıf ve 
#parent class 


#child class  bu classlar temel sınıflardan oluşur.

class Person:
    def __init__(self,name,surname,age) -> None:
        self.name = name
        self.surname = surname
        self.age = age
        print("Person Nesnesi Türetildi.")

class Student(Person):
    pass
 

class Teacher(Person):
     pass


# t1 = Teacher()
p1 = Person("Sefa","Pınar",40)
# s1 = Student()

print(p1.name,p1.surname,p1.age)