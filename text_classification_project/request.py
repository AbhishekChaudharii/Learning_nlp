import requests

url = 'http://localhost:5000/api'

r = requests.post(url,json={'text':"Indian economy faces serious challenges"})
print(r.json())