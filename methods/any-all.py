# sonuc = all([True,True,False])
# sonuc = any([True,False,True])




# and => True & True =>All() =>All()
# Or => True or False =>True() =>Any()



sayilar = [0,1,2,3,4,5,6,7]
sonuc = any([bool(sayi) for sayi in sayilar])
sonuc = all([bool(sayi) for sayi in sayilar if sayi%2==1])
sonuc = all([sayi%2==0 for sayi in sayilar])


print(sonuc)