import random

# result = dir(random)
# result = help(random)

result = random.random()
result = random.uniform(1,10)

result = random.randint(1,111)


names = ['Sefa','Pınar','Deniz','Ahmet','Cenk']
result = names[random.randint(0,len(names)-1)]

result = random.choice(names)
  #Listeden rastgele bir elemanı bizlere geri getirir.







liste = list(range(10))

random.shuffle(liste)
print(result)


