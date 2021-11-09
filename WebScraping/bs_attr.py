from bs4 import BeautifulSoup

with open("WebScraping/index.html") as file:
    html_doc= file.read()

obj  = BeautifulSoup(html_doc,"html.parser")

sonuc = obj.div
sonuc = obj.div('div')

sonuc = obj.find(id="div1")
sonuc = obj.find(id ="div2")

sonuc = obj.find(class_="grup1")

sonuc = obj.select('#header')
sonuc = obj.select('#div1')

sonuc = obj.select_one('.id')


sonuc = obj.div.attrs[id]
sonuc = obj.get_text(strip=True)  #sayfada bulunan bütün textleri getirir.


for a in obj.find_all('a'):
    print(a.get('href'))
print(sonuc)