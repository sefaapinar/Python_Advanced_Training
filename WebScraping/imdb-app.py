import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/moviemeter/?sort=rk,asc&mode=simple&page=1"



html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

list = soup.find('tbody',{"class":"lister-list"}).find_all("tr",limit=10)
# count = 1


for tr in list:
    title = tr.find("td",{"class":"titleColumn"}).find("a").text
    year = tr.find("td",{"class":"titleColumn"}).find("span").text.strip("()")
    rating = tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text


print(f"- film: {title} yıl: {year} değerlendirme: {rating}")
# count+=1