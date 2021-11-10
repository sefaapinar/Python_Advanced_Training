import requests
from bs4 import BeautifulSoup

search_input = input('aramak istediğiniz kelime : ').replace(' ', '+')
# link = "https://www.google.com/search?q=" + search_input
link = "https://www.google.com/search?q=" + "python"

headerParams = {"user-agent":""}

response = requests.get(link, headers= headerParams)

soup = BeautifulSoup(response.content,"html.parser")
results = soup.find_all('div', class_="rc")

for div in results:
    anchor = div.find('a')

    link = anchor['href']
    text = anchor.find('h3').string

    description = anchor.parent.next_sibling.find('span').text

    print(link,description)