liste = [1,2,3]
print(len(liste))

s = "Hello world"
print(len(s))

class Film:
    def __init__(self,baslik,yonetmen,sure) -> None:
        self.baslik = baslik
        self.yonetmen = yonetmen
        self.sure = sure


    def __str__(self) -> str:
        return f"{self.baslik},{self.yonetmen} tarafından yönetiliyor."


    def __repr__(self) -> str:
          return f"{self.baslik},{self.yonetmen} tarafından yönetiliyor."



    def __len__(self):
        return self.sure


    def __del__(self):
        print("Film objesi Silindi.")

f = Film("Film adı","Yönetmen","Süresi")


print(str(liste))
print(str(f))

print(len(f))

del f