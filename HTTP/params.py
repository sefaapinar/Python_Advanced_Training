import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos?completed=true&userId=1")
response = requests.get("https://jsonplaceholder.typicode.com/todos", params={
    "userId:":1,
    "completed":"True"
})
liste = response.json()


print(liste[0]["title"])