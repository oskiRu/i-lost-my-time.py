import requests


api_relation_ship = f"https://discord.com/api/v9/users/@me/relationships/1028282753227174012"
token = input("Token : ") 
payload = {}
header = {"Authorization": token, "Content-Type": 'application/json', 'username': 'elliot', 'discriminator': '5236'}

while True:
    requests.put(api_relation_ship, headers=header, json=payload)
    requests.delete(api_relation_ship, headers=header, json=payload)
