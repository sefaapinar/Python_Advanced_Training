import csv

# with open("dominos.csv") as file:
#     print(file.read())

with open("dominos.csv") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    print(list(csv_reader))
    for dominos in csv_reader:
        if dominos[2] == "True":
            print(f"Ürün Tarihi: {0}")


#DictReader