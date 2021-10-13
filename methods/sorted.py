sayilar =[1,45,22,3,4,666,66,5,123]
# sayilar.sort()

sonuc = sorted(sayilar, reverse=True)
sonuc = sorted((1,45,22,3,4,666,66,5,123))

users = [
    {"username":"sefaapinar","tweets":["tweet 1","tweet 3"],"email":"info@gmail.com"},
    {"username":"ahmetturan","tweets":["tweet 1","tweet 2"]}, 
    {"username":"tamerpinar","tweets":[],"phone":"0544423112"}
]

sonuc = sorted(users, key=len)
sonuc = sorted(users, key = lambda user: user["username"])

sonuc = sorted(users, key=lambda user: len(user["tweets"]))


print(sonuc)
print(sayilar)
print(users)