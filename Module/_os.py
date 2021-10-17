from os import *
import os

from datetime import *

# result = dir(os)
# result = os.name #İşletim sistemini getirir.  #OS = Operation System
# result = os.getcwd #Dosya ismini getirir.

# os.chdir('C:\\')

#Klasör Oluşturma
# os.mkdir("newdirectory")

# os.makedirs("newdirectory/yeniklasör") #Dosya içerisine yeni klasör oluşturur.

#Listeleme İşlemleri

# result = os.listdir()

# #Filtreleme işlemleri

# for dosya in os.listdir():
#     if dosya.endswith('.py'):
#         print(dosya)
# print(result)

# result = os.stat("_datetime.py")
# result = result.st_size/1024
# print(result)

# os.system("notepad.exe")

# os.rename("yeniklasör","osDeneme") Dosya adı değiştirme.


# os.rmdir("osDeneme")


# path modül kullanımı


result = os.path.abspath("_os.py")
result =  os.path.dirname

print(result)

