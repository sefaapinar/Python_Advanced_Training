# #kendisine iki sayidan büyük olanı bulma

# def karsilastirma(a,b):
#     if(a>b):
#         return "a'b den büyüktür."
#     elif(b>a):
#         return "b-a'dan büyüktür"
#     return "a b ye eşittir."
    
# sonuc = karsilastirma(10,23)
# print(sonuc)

#######ÖRNEK 2#####

# #kendisine gönderilen bir string bilgi içinde her karakter kaçar kez tekrarlanmış bulunuz.

# def karakterSayisiniBul(s):
#     return {letter:s.count(letter) for letter in s}

# sonuc = karakterSayisiniBul("Javascript")
# print(sonuc)


####ÖRNEK 3

def update_list(list,command,position,value=None):
    if(command =="remove" and position =="end"):
        return list.pop()
    elif(command == "remove" and position =="beginning"):
        return list.pop(0)
    elif(command=="add" and position=="end"):
        list.append(value)
        return list
    elif(command=="add" and position=="beginning"):
        list.insert(0,value)
        return list

sonuc = update_list([1,2,3],"add","end",3)
print(sonuc)

####3

def contains_blue(*args):
    if"blue" in args:
        return True
    return False

sonuc = contains_blue("blue","yellow","red")
print(sonuc)