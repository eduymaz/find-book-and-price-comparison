import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/api"

st.title("Find Book API - Kitap Arama ve Karşılaştırma")

menu = ["Bulunabilirlik Sorgula"]
choice = st.sidebar.selectbox("Menü", menu)

platform_options = ["Kitapyurdu", "Kırmızı Kedi"]
selected_platforms = st.sidebar.multiselect(
    "Veri Çekilecek Siteler",
    platform_options,
    default=platform_options
)

if choice == "Bulunabilirlik Sorgula":
    st.header("Bulunabilirlik ve Fiyat Sorgula")
    title = st.text_input("Kitap Adı (zorunlu)")
    compare = st.checkbox("Fiyat Karşılaştır")
    if st.button("Sorgula"):
        if not title:
            st.warning("Lütfen kitap adı girin.")
        else:
            r = requests.get(f"{API_URL}/books", params={"title": title})
            if r.status_code == 200:
                books = r.json()
                if not books:
                    st.info("Sonuç bulunamadı.")
                filtered_books = [book for book in books if book['platform'] in selected_platforms]
                for book in filtered_books:
                    st.write(f"**{book['title']}** - {book['author']}")
                    st.write(f"Yayın Evi: {book['publisher']}")
                    st.write(f"Fiyat: {book['price']}")
                    st.write(f"Platform: {book['platform']}")
                    url = book['url']
                    if url.startswith("/index.php") or url.startswith("/kitap/"):
                        url = "https://www.kitapyurdu.com" + url
                    elif url.startswith("/arama") or url.startswith("/product/"):
                        url = "https://www.kirmizikedi.com" + url
                    st.write(f"Satın Al: [Git]({url})")
                    st.write("---")
                if compare and filtered_books:
                    st.subheader("Fiyat Karşılaştırması")
                    # Aynı kitap adını içerenler arasında en düşük fiyatı bul
                    price_list = []
                    for book in filtered_books:
                        try:
                            price = float(str(book['price']).replace("TL", "").replace(",", ".").strip())
                            price_list.append((book['platform'], price, book['url']))
                        except:
                            continue
                    if price_list:
                        price_list.sort(key=lambda x: x[1])
                        st.write("En uygun fiyat:")
                        for plat, price, url in price_list:
                            st.write(f"{plat}: {price} TL - [Satın Al]({url})")
                    else:
                        st.info("Fiyat karşılaştırması için uygun veri bulunamadı.")
            else:
                st.error("Sorgulama başarısız.")
