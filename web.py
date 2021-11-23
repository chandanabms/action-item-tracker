import requests 
import json 
response = requests.get('https://jsonplaceholder.typicode.com/users') 
(response.text)
res = json.loads(response.text)
for i in res:
    if id == i["id"]:
        i+1
        name = input('What is your name?')
        username = input('What is your username?')
        email = input('What is your email?')
        with open("op3.json", "a") as data:
            information = [{'id': i ,'name': name, 'username':username, 'email':email, }]
            data.write(json.dumps(information))
            data.close()