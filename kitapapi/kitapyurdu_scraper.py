import requests
from bs4 import BeautifulSoup

def search_kitapyurdu(query):
    """
    Kitapyurdu'nda kitap araması yapar ve ilk 5 sonucu döndürür.
    Dönüş: [{title, author, price, publisher, url}]
    """
    url = f"https://www.kitapyurdu.com/index.php?route=product/search&filter_name={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    }
    resp = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(resp.text, "html.parser")
    results = []
    for item in soup.select(".product-cr")[:5]:
        title = item.select_one(".name a").get_text(strip=True) if item.select_one(".name a") else ""
        author = item.select_one(".author a").get_text(strip=True) if item.select_one(".author a") else ""
        publisher = item.select_one(".publisher a").get_text(strip=True) if item.select_one(".publisher a") else ""
        price = item.select_one(".price span.value").get_text(strip=True) if item.select_one(".price span.value") else ""
        # Kitap linki (tam adres olmalı)
        book_url = ""
        name_a = item.select_one(".name a")
        if name_a and name_a.has_attr('href'):
            href = name_a['href']
            if href.startswith("http"):
                book_url = href
            else:
                book_url = "https://www.kitapyurdu.com" + href
        results.append({
            "title": title,
            "author": author,
            "publisher": publisher,
            "platform": "Kitapyurdu",
            "price": price,
            "url": book_url
        })
    return results

def search_kirmizikedi(query):
    """
    Kırmızı Kedi'de kitap araması yapar ve ilk 5 sonucu döndürür.
    Dönüş: [{title, author, price, publisher, url}]
    """
    url = f"https://www.kirmizikedi.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(resp.text, "html.parser")
    results = []
    for item in soup.select("div.product-box")[:5]:
        # Kitap başlığı
        title = ""
        title_span = item.select_one(".product-name-label")
        if title_span:
            title = title_span.get_text(strip=True)
        # Yayınevi
        publisher = ""
        publisher_span = item.select_one(".brand-name")
        if publisher_span:
            publisher = publisher_span.get_text(strip=True)
        # Fiyat
        price = ""
        price_span = item.select_one(".product-price .price")
        if price_span:
            price = price_span.get_text(strip=True)
        # Kitap linki
        book_url = ""
        a_tag = item.select_one("a[title][href]")
        if a_tag:
            book_url = "https://www.kirmizikedi.com" + a_tag['href']
        results.append({
            "title": title,
            "author": "",  # Ana listede yazar yok
            "publisher": publisher,
            "platform": "Kırmızı Kedi",
            "price": price,
            "url": book_url
        })
    if not results:
        print("[DEBUG] Kırmızı Kedi'den sonuç gelmedi. HTML yapısı değişmiş olabilir.")
    return results
