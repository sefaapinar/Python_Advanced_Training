def displayUser(*args):
    print(type(args))

displayUser()

def displayUser(**kwargs):
    print(type(kwargs))
    print(kwargs)

displayUser(username = "Sefa Pinar", email="sefapinar@gmail.com")

