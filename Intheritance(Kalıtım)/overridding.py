class NewDict(dict):
    def __repr__(self) -> str:
        print('repr methodundan bir mesaj var')
        return super().__repr__()

    def __missing__(self,key):
        print("olmayan key bilgisi istiyorsunuz.")

    def __getitem__(self,key):
        print("bir elemanı çağırıyorsunuz.")
        return super().__getitem__(key)

    def __setitem__(self,key,value) -> None:
        print("Listeye eleman ekliyoruz.")
        return super().__setitem__(k, v)

    def __contains__(self, o: object) -> bool:
        print("Listede eleman arayamazsınız.")
        return super().__contains__(o)

data = NewDict({"first":"Sefa","last":"Pınar"})


data["First"]
print(data)

print(data)

