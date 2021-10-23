class User:
    active_users = 0

    @classmethod
    def display_active_users():
        return f"Şuanda aktif {User.active_users} user var."

    def __init__(self,firstname,lastname) -> None:
        self.firstname = firstname
        self.lastname = lastname
        User.active_users +=1
    def fullname(self):
        return f"{self.firstname} {self.lastname}"



class Moderator(User):
    def __init__(self, firstname, lastname,community) -> None:
        super().__init__(firstname, lastname)
        self.community = community



print(User.display_active_users())
u1 = User("Ali","Korkmaz")
m1 = Moderator("Yağmur","Korkmaz","IoT Topluluğu")
print(User.display_active_users())

# print(isinstance(u1, User))
# print(isinstance(u1, Moderator))
# print(isinstance(m1, User))
