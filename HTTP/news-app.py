import requests 

headlines_url = "https://newsapi.org/v2/top-headlines?country=tr&apiKey="

api_key="593b9581160b493292f2475ce7630dd2"


response = requests.get(headlines_url,params={
    "apiKey":api_key,
    "country":"tr"
})


haberler = response.json()["articles"]

print(haberler[0])

for i in haberler:
    print(i["source"]["name"])
    print(i["title"])
    print(i["url"])