

import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/fotograf-ve-kamera/fotograf-makinesi"
html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")
a = soup.find_all("li", {"class": "column"})
count = 1
for li in a:
    title = li.div.a.h3.text.strip()
    oldprice = li.find("div", {"class": "proDetail"}).find_all("a")[0].text.strip()
    link = li.div.a.get("href")

    print(f"{count} - Ürün: {title} Fiyat: {oldprice} Ürün Linki : {link}")
    count += 1

    # ÇEŞİTLENDİRİLEREK  GELİŞTİREBİLİR ESKİ YENİ FİYAT İSTENİLEN GİBİ
