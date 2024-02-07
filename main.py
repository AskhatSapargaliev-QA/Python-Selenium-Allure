"""
Создание покемона
"""
import requests

URL='https://api.pokemonbattle.me:9104'
HEADER={'Content-Type': 'application/json','trainer_token':'71cee82101e4055431a7544a53ef1ea5'}

#body={
 #   "name": "Орк",
  #  "photo": "https://dolnikov.ru/pokemons/albums/068.png"
#}
#body={
 #   "pokemon_id": "29683",
  #  "name": "Вагнер",
#}
#body={
#    "pokemon_id": "29683"
#}
# response=requests.post(url=f'{URL}/pokemons',json=body,headers=HEADER,timeout=10)
# print(f'Статус код: {response.status_code}.Сообщение:{response.json()['message']}')

#response=requests.put(url=f'{URL}/pokemons',json=body,headers=HEADER,timeout=10)
#print(f'Статус код: {response.status_code}.Сообщение:{response.json()['message']}')

#response=requests.post(url=f'{URL}/trainers/add_pokeball',json=body,headers=HEADER,timeout=10)
#print(f'Статус код: {response.status_code}.Сообщение:{response.json()['message']}')

response=requests.get(url=f'{URL}/trainers',params={'level':1},timeout=5)
print(f'Статус код: {response.status_code}')
