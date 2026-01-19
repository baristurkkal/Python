import requests
import json  # JSON çıktısını güzel göstermek için

url = "https://api.github.com/users/octocat"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # JSON çıktısını düzenli (pretty print) olarak yazdır
    print(json.dumps(data,indent=4))
else:
    print("API çağrısı başarısız oldu. Status kod:", response.status_code)

