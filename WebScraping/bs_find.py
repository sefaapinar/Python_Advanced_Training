from bs4 import BeautifulSoup


with open("WebScraping/index.html") as file:
    html_doc = file.read()


obj = BeautifulSoup(html_doc,"html.parser")

sonuc = obj.find
sonuc = obj.find('div')
sonuc = obj.find_all("div")
# sonuc = obj.find_all('div')[1].ul.find_all('li')



# for div in obj.find_all('div'):
#     if div.h2.a !=None:
#         print(div.h2.a.string.strip())

print(sonuc)