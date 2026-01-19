import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # BBC'de haber başlıkları genelde <h2> tag'leri içinde
    headlines = soup.find_all("h2")
    
    print("BBC News Başlıkları:")
    for h in headlines[:10]:  # ilk 10 başlığı yazdıralım
        print("-", h.get_text(strip=True))
else:
    print("Siteye bağlanılamadı. Status kod:", response.status_code)

