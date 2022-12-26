import requests
from pprint import pprint


def filter_hero(hero):
    if (hero["name"] == "Hulk") or (hero["name"] == "Captain America") or (hero["name"] == "Thanos"):
        return True
    else:
        return False


json_response = requests.get('https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json', params=b'postId=1')
hero_dict = json_response.json()
out_filter = list(filter(filter_hero, hero_dict))
max_int = out_filter[0]
for hero in out_filter:
    if hero["powerstats"]["intelligence"] > max_int["powerstats"]["intelligence"]:
        max_int = hero
        
print("Cамый умный(intelligence) из трех супергероев -", max_int["name"])