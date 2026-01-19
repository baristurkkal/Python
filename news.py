import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"

response = requests.get(url, timeout=10)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

# BBC genelde h3 başlık kullanır
headlines = soup.find_all("h2")

for i, h in enumerate(headlines, start=1):
    text = h.get_text(strip=True)
    if text:
        print(f"{i}. {text}")

