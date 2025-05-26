# Find Book API

Kullanıcıların kitap arayabileceği, fiyat ve bulunabilirlik karşılaştırması yapabileceği bir REST API.

## Kurulum

1. Terminalde proje klasörüne gelin.
2. Kurulum scriptini çalıştırın:

```bash
bash install.sh
```

3. Sunucuyu başlatın:

```bash
source venv/bin/activate
python manage.py runserver
```

## API Uç Noktaları

- `GET /api/books` : Kitapları listele (filtreleme için: ?title=, ?author=, ?publisher=, ?category=)
- `GET /api/books/{id}` : Belirli kitabın detayları
- `GET /api/books/availability?title=...` : Kitabın platformlardaki bulunabilirliği ve fiyatları
- `GET /api/books/recommendations?category=...` : Kategoriye göre öneriler

## Veri

Sahte kitap verileri `data/sample_books.json` dosyasında tutulur. Gerçek veritabanına yüklemek için ek script veya yönetim komutu eklenebilir.

## Komutlar ve Dosya Açıklamaları

### Proje Kurulumu ve Çalıştırma

1. Sanal ortam ve bağımlılık kurulumu:

```bash
bash install.sh
```

2. Sanal ortamı aktifleştir:

```bash
source venv/bin/activate
```

3. Veritabanı migrasyonları (install.sh ile otomatik yapılır, gerekirse tekrar çalıştır):

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Admin kullanıcısı oluşturma (install.sh ile otomatik, elle istersen):

```bash
python manage.py createsuperuser
```

5. Örnek kitap verilerini yükle:

```bash
python manage.py load_sample_books
```

6. Sunucuyu başlat:

```bash
python manage.py runserver
```

### Ana Dosyalar ve Görevleri

- `manage.py`: Django yönetim komutlarını çalıştırmak için ana dosya.
- `findbook/settings.py`: Proje ayarları.
- `findbook/urls.py`: URL yönlendirmeleri (ana sayfa, API, admin).
- `kitapapi/models.py`: Kitap, platform, kategori ve bulunabilirlik modelleri.
- `kitapapi/views.py`: API uç noktaları (kitap liste, detay, öneri, bulunabilirlik).
- `kitapapi/serializers.py`: Model verilerini JSON'a dönüştüren serializer'lar.
- `kitapapi/management/commands/load_sample_books.py`: JSON'dan veritabanına örnek veri yükleme komutu.

### Ana Sayfa

Sunucu çalışırken http://127.0.0.1:8000/ adresine giderseniz hoş geldiniz mesajı ve API yönlendirmesi göreceksiniz.

API uç noktaları için örnekler ve daha fazla bilgi yukarıda verilmiştir.

## Geliştirici Notları
- Backend: Python, Django REST Framework
- Veritabanı: SQLite (varsayılan)
