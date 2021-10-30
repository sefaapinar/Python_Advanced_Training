from csv import DictWriter

with open("products.csv","w") as file:
    headers = ["ProductName","Price","IsPublished","Category","Reviews"]
    csv_writer = DictWriter(file,headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "ProductName":"Iphone 7",
        "Price":4000,
        "IsPublished":"True",
        "Category":"Telephon",
        "Reviews":4.4,

        "ProductName":"Iphone 9",
        "Price":4000,
        "IsPublished":"True",
        "Category":"Telephon",
        "Reviews":4.4,
        
        "ProductName":"Iphone 8",
        "Price":4000,
        "IsPublished":"True",
        "Category":"Telephon",
        "Reviews":4.4
    })