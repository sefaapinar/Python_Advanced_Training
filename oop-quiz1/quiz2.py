import random
class Question:
    def __init__(self,answer,text,choices) -> None:
        self.answer = answer
        self.text = text
        self.choices = choices

    def CheckAnswer(self,answer):
        if answer not in self.choices:
            raise ValueError('Hatalı Bilgi Girdiniz.')

        return self.answer == answer

class Quiz:
    def __init__(self,question) -> None:
            self.question = random.shuffle(question)
            self.questionIndex = 0
            self.score = 0

    def getQuestion(self):
        return self.question[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()

        print(f"Soru {self.questionIndex} + 1:{question.text}")

        for q in question.choices:
            print("-" + q)

        answer = input('cevap: ')
        if (question.checkAnswer(answer)):
            self.score +=1
        
        self.questionIndex +=1

        if len(self.question) == self.questionIndex:
            self.displayScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def displayScore(self):
        print("Score",self.score)

    def displayProgress(self):
        totalQuestion = len(self.question)
        questionNumer = self.questionIndex + 1

        print("Toplam {totalQuestion} sorunun {questionNumber}. sorusundasınız.".center(100,'*'))


        self.displayQuestion()

q1 = Question("en iyi programlama dili hangisidir?",["python","c#","java","dart"],"python")
q2 = Question("en popüler programlama dili hangisidir?",["python","java","c#","dart"],"python")
q3 = Question("en çok kazandıran programlama dili hangisidir?",["python","java","dart","c#"],"python")

sorular = [q1,q2,q3]

quiz = Quiz(sorular)

print(quiz.displayQuestion())



