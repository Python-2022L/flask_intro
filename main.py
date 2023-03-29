import requests

r = requests.get('http://127.0.0.1:4180/')
print(r.json())