from csv import writer,reader
import csv
from os import read

# with open("cars.csv","a") as file:

# with open("dominos.csv") as file:
#     csv_reader = reader(file)
#     with open("new-products.csv","w") as file:
#         csv_writer = writer(file)
#         for dominoss in csv_reader:
#             csv_writer.writerow([p.upper for p in dominoss])


with open("dominos.csv","r+") as file:
    csv_reader = reader(file)
    csv_writer = writer(file)

    next(csv_reader)
    dominos = [p[0],p[1] for p in csv_reader]
    print(dominos)






    # csv_writer = writer(file)
    # csv_writer.writerow(["Toyota","Rav4"])
    # # csv_writer = writer(file)
    # csv_writer.writerows(["Marka","Model"],["Toyota","Corolla"],["Renault","Clio"])
    # csv_writer.writerow(["Marka","Model"])
    # csv_writer.writerow(["Toyota","Yaris"])
    # csv_writer.writerow(["Toyota","Corolla"])

