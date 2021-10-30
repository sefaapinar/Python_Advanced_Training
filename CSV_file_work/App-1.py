import csv
from types import CellType

def add_user(first_name,last_name):
    with open("users.csv","a",encoding="UTF-8") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([first_name,last_name])

# add_user("Sefa" ,"Pınar")

def get_user():
    with open("users.csv") as file:
        csv_reader = csv.DictReader(file)
        for user in csv_reader:
            print(f'{user["FirstName"]} {user["LastName"]}')


def find_user(first_name,last_name):
    with open("users.csv") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)

find_user("Sefa","Pınar")