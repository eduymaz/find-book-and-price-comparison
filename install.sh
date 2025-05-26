#!/bin/bash
# Proje kurulum scripti

echo "✅ find-book-api kurulumu başlatılıyor..."

# Sanal ortam oluştur
python3 -m venv venv
source venv/bin/activate

# Gereken paketleri yükle
pip install --upgrade pip
pip install -r requirements.txt

# Veritabanı başlat
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --noinput || true

echo "✅ Kurulum tamamlandı. Sunucu başlatmak için:"
echo "source venv/bin/activate && python manage.py runserver"