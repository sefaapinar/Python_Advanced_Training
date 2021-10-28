# with open("markalar.txt","a",encoding="UTF-8") as file:
# #     file.write("6-bmw")

# with open("markalar.txt","r+",encoding="UTF-8") as file:
#         markalar = file.read()
#         markalar = "1-Toyata\n" + markalar
#         print(markalar)
#         file.seek(0)
#         file.write(markalar)

from os import read


with open("markalar.txt","r+",encoding="UTF-8") as file:
    markalar = file.readlines()
    markalar.insert(2,"3-Renault Clio\n")
    file.seek(0)
    # for marka in markalar:
    #     file.write(marka)
    file.writelines(markalar)

# with open("markalar.txt") as file:
#     print(file.read())