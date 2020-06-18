import requests

# example how to call the api
url = 'http://localhost:5000/results'
r = requests.post(url, json={'short_code':"CBgHs1Xjgin", 'max_comments':"10"})

print(r.json())