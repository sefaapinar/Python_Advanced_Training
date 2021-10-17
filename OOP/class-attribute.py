class User:
    active_users = 0
    def __init__(self,name,last,age) -> None:
        self.name = name
        self.age = age
        self.last = last
        User.active_users +=1

    def full_name(self):
        return f"{self.name} {self.last}"

    def logout(self):
        User.active_users -=1
        return f"{self.full_name()} uygulamadan çıkış yaptı"

print(User.active_users)
userA = User("Sefa","Pınar",21)
userB = User("Sevval","Pınar",22)
print(userA.full_name)
print(userB.full_name)