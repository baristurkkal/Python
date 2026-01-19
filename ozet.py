import os
import requests
from bs4 import BeautifulSoup
from openai import OpenAI

# OpenAI client (API key ortam değişkeninden okunuyor)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 1. BBC News sayfasını indir
url = "https://www.bbc.com/news"
response = requests.get(url)

if response.status_code != 200:
    print("BBC sitesine bağlanılamadı. Status kod:", response.status_code)
    exit()

soup = BeautifulSoup(response.text, "html.parser")

# 2. Haber başlıklarını çek (BBC genelde <h2> içinde tutuyor)
headlines = [h.get_text(strip=True) for h in soup.find_all("h2")]

print("BBC Haber Başlıkları ve Özetleri:\n")

# İlk 5 haberi özetleyelim
for i, headline in enumerate(headlines[:5], 1):
    print(f"{i}. {headline}")
    
    # 3. ChatGPT ile özet çıkarma
    response = client.chat.completions.create(
        model="gpt-4o-mini",   # hızlı model
        messages=[
            {"role": "system", "content": "Sen bir haber özetleyicisin."},
            {"role": "user", "content": f"Bu başlığı haber olarak düşün ve 1-2 cümlelik kısa özet yaz:\n\n{headline}"}
        ]
    )
    
    summary = response.choices[0].message.content
    print("   Özet:", summary, "\n")

