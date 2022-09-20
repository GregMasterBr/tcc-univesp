import json
import requests

url = 'https://Client.atlassian.net/wiki/rest/api/content/87440'
headers = {'Content-Type': "application/json", 'Accept': "application/json"}
f = open("file.html", "r")
html = f.read()

data={}
data['id'] = "87440"
data['type']="page"
data['title']="Data Page"
data['space']={"key":"AB"}
data['body'] = {"storage":{"representation":"storage"}}
data['version']={"number":4}

print(data)

data['body']['storage']['value'] = html

print(data)

res = requests.put(url, json=data, headers=headers, auth=('Username', 'Password'))

print(res.status_code)
print(res.raise_for_status())