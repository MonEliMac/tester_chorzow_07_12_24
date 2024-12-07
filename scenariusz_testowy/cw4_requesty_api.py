import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
# print(response)

if response.status_code == 200:
    print("Jupi! Strona jest ok")
    print(f"Dane użytkownikow to {response.json()}")
else:
    print(f"Ups, cos poszlo nie tak, kod bledu to {response.status_code}")