import requests

response = requests.get('https://randomuser.me/api/?results=5&nat=tr')
data = response.json()

for person in data['results']:
    isim = person['name']['first'] + ' ' + person['name']['last']
    print(isim)