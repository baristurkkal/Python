import requests
r  = requests.get("https://jsonplaceholder.typicode.com/posts/1")
dic = {}
data = r.json()
dic = data
print(dic["title"],dic["body"],sep="\n")
