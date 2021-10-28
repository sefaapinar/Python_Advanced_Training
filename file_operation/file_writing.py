
with open("/users/sefa/desktop/newFile.txt","w",encoding="UTF-8") as file:

    file = open("newFile.txt","w",encoding="UTF-8")
    file.write("Sefa Pınar\n")
    file.write("Meryem Pınar\n")
    file.write("Tamer Pınar\n")


print(file)


with open("newFile.txt") as file:
    print(file.read())
#Eğer konumda aynı dosya varsa dosyayı siler ver yeni dosya oluşturur.
#(write) = w
# Dosyayı konumda oluşturur.

