import requests
from requests.models import Response

url="http://api.weatherapi.com/v1/current.json"

accces_key="28f5bde6f2c94ea8a92190826210511"

guess = requests.get(url, params={
    "key":accces_key,
    "q":"istanbul"
})

sonuc = guess.json()

print(sonuc)