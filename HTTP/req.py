import requests
import json


response = requests.get("https://jsonplaceholder.typicode.com/todos")

sonuc = response
sonuc = type(response)
sonuc = response.status_code
sonuc = response.headers
sonuc = response.headers["Content-Type"]
sonuc = response.url
sonuc = response.encoding
sonuc = response.text
sonuc = json.loads(response.text)
sonuc = type(sonuc)
print(sonuc)