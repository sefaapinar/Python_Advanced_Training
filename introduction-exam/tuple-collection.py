_list=[1,2,3]
_tuple=(1,2,3)

print(type(_list))
print(type(_tuple))

print(len(_tuple))
print(len(_list))

_list.append(3)
print(_list)

#Tuple listelerinde listeye  veri kümesine daha sonradan veri eklenemez.

_t = tuple([2,3,4])  #Liste elemanlarını tuple çevirme.
print(type(_t))
print(_t)