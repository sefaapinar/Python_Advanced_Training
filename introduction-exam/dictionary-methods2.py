from typing import NewType


players = {}
    
    


id = input('Oyuncu No:')
name = input('Oyuncu Adı:')
country = input('Ülke: ')
currentTeam = input('Güncel Takım: ')
yearOfBirthDay = input('Doğum Yılı: ')

players.update({
    id:{
        "name":name,
        "country":country,
        "currentTeam": currentTeam,
        "yearOfBirthDay": yearOfBirthDay
    }
})

id = input('Aramak istediğiniz oyuncu bilgisi:')
player = players.get(id)
print(player)

#ID'ye göre arama.



id = input('Silmek istediğiniz oyuncunun numarasını yazınız: ')
players.pop(id)

#ID'ye göre silme.
print(players)