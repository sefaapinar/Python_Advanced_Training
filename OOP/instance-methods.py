class Person:

    #Yapıcı Method #Constructor
    def __init__(self,name,surname,year):
        #Object Attribute
        self.name = name
        self.surname = surname
        self.year = year
    
    #Instance Method
    def intro(self):
        return f"Benim Adım {self.name} ve soy adım {self.surname} doğduğum yıl ise {self.year}"

    def calculate_age(self):
        return f"{2021-self.year}"
#Objec Instance
p1 = Person("Sefa","Pınar",2000)
p2 = Person("Fehmi","Kasmir",1999)

print(p1.intro())
print(p2.intro())

print(p1.calculate_age())