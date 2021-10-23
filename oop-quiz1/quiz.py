# Quiz App

# Question sınıfı
#   Instance Attributes
#       - text, choices, answer
#   Instance Methods
#       - q1.checkAnswer('python') => True ya da False

# q1 = Question("en iyi programlama dili hangisidir?",["python","c#","java","dart"],"python")
# q2 = Question("en popüler programlama dili hangisidir?",["python","java","c#","dart"],"python")
# q3 = Question("en çok kazandıran programlama dili hangisidir?",["python","java","dart","c#"],"python")

# sorular = [q1,q2,q3]

# Quiz sınıfı
#   Instance Attributes
#       - questions, questionIndex, score
#   Instance Methods
#       - getQuestion()         => questionIndex' e göre question nesnesi getirir.
#       - displayQuestion()     => getQuestion() ile alınan nesneyi gösterir.
#       - loadQuestion()        => Testi başlatır.
#       - displayScore()        => Score bilgisini gösterir.
#       - displayProgress()     => Testdeki ilerlemeyi gösterir. (5 sorunun 2.sorusundasınız.)


# quiz = Quiz(sorular)

class Question:
    def __init__(self,text,choices,answer) -> None:
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self,answer):
        if answer not in self.choices:
            raise ValueError("Hatalı Bilgi Girdiniz.")
        return self.answer == answer
        
q1 = Question("En iyi programlama dilleri nedir?",["Python","C#","Java","Angular","Flutter"], "Python")

print(q1.text)
print(q1.answer)
print(q1.choices)


sonuc = q1.checkAnswer('Python')
print(sonuc)