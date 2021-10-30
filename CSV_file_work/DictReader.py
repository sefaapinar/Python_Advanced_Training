from csv import DictReader
import csv

with open("dominos.csv") as file:
    csv_reader = DictReader(file)

    for dominos in csv_reader:
        print(dominos)
