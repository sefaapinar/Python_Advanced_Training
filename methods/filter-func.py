yaslar = [5,11,33,44,32,46]

def yetiskinmi(x):
    if(x<18):
        print("Yaşınız 18 den küçük")
    else:
        print("Yaşınız 18 den büyük. Yetişkinsiniz")
sonuc = list(filter(yetiskinmi,yaslar))

sonuc = list(filter(lambda x: x>=18, yaslar))
print(sonuc)


sayilar =[1,2,3,4,5,6,7,8]

sonuc=list(filter(lambda x: x%2==0, sayilar))
print(sonuc) 

users = [
    {"username":"sefaapinar","tweets":["tweet 1","tweet 3"]},
    {"username":"ahmetturan","tweets":["tweet 1","tweet 2"]}, 
    {"username":"sefaapinar","tweets":[]}
]

sonuc = list(filter(lambda u: len(u["tweets"])>0, users))
sonuc = list(map(lambda u:u["username"].upper(),filter(lambda u: len(u["tweets"])>0, users)))



sonuc =[user["username"].uppper() for user in users if len(users["tweets"])>0]
print(sonuc)