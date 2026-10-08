import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

if response.status_code == 200:
    print("api call success")

    users = response.json()
    print("User names:")
    for user in users:
        print(user["name"])

else:
    print("api call error")

    