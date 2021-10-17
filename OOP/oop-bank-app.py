class BankAccount:
    def __init__(self,name) -> None:
        self.owner = name
        self.balance = 0.0

    def getBalance(self):
        return self.balance

    def deposit(self,amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self,amount):
        self.balance -=amount
        return self.balance

hesap = BankAccount("Sefa Pınar")



print(hesap.getBalance)
hesap.deposit(2000)
print(hesap.getBalance)
hesap.withdraw(500)
print(hesap.getBalance)