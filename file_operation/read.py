# file = open("msg.txt")

try:
    with open("msg.txt",encoding="utf-8") as file:
        # print(file.read(10))
        # print(file.tell())
        # print(file.read(10))
        for i in file:
            print(i, end="")
except FileNotFoundError as e:
    print("Dosya Okuma Hatası",e)

finally:
    print("Dosya Kapandı.")
