from bs4 import BeautifulSoup

with open("WebScraping/index.html") as file:
    html_doc= file.read()

obj  = BeautifulSoup(html_doc,"html.parser")
sonuc = obj 
sonuc = obj.prettify
sonuc = obj.title


sonuc = obj.body
sonuc = obj.body.h1  #body etiketi altında h1'i getirir.
print(sonuc)

