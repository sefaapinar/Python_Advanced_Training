import requests 
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://github.com/sefaapinar')

soup = BeautifulSoup(response.text,"html.parser")

github = (soup.find_all(class_="position-relative"))

github_image= github('img')['src']


#Devam Edilecek.