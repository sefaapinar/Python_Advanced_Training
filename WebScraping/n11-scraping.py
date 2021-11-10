import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"

html = requests.get(url).content

soup = BeautifulSoup(html,"html.parser")

list = soup.find_all("li",{"class":"column"},limit=1)

for li in list:
    name = li.div.a.h3.text
    link = li.div.a.get("href")
    oldprice = li.find("div",{"class":"proDetail"}).find_all("a")[0]
    newprice = li.find("div",{"class":"proDetail"}).find_all("a")[1]

  
print(f"name:{name} link: {link} old price:{oldprice} new price:{newprice}")
