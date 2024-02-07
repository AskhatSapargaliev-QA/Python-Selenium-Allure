import requests
import pytest

URL='https://api.pokemonbattle.me:9104'
HEADER={'Content-Type': 'application/json','trainer_token':'71cee82101e4055431a7544a53ef1ea5'}

def test_get_trainers():
    """
    GET trainers status code 200
    """
    response=requests.get(url=f'{URL}/trainers',params={'trainer_id':3656},timeout=5)
    assert response.status_code == 200

def test_get_trainers():
    """
    GET trainers trainer name
    """
    response=requests.get(url=f'{URL}/trainers',params={'trainer_id':3656},timeout=5)
    assert response.json()["trainer_name"] == 'Асхат'
    
    
    
    



