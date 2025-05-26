import json
import os
from django.core.management.base import BaseCommand
from kitapapi.models import Book, Platform, Category, BookAvailability
from django.conf import settings

class Command(BaseCommand):
    help = 'Load sample books from data/sample_books.json into the database.'

    def handle(self, *args, **options):
        file_path = os.path.join(settings.BASE_DIR, 'data', 'sample_books.json')
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for book_data in data['books']:
            category_name = book_data.get('category', 'Diğer')
            category, _ = Category.objects.get_or_create(name=category_name)
            book, _ = Book.objects.get_or_create(
                title=book_data['title'],
                author=book_data['author'],
                isbn=book_data['isbn'],
                publisher=book_data['publisher'],
                year=book_data['year'],
                category=category
            )
            for plat in book_data.get('platforms', []):
                platform, _ = Platform.objects.get_or_create(name=plat['name'])
                BookAvailability.objects.update_or_create(
                    book=book,
                    platform=platform,
                    defaults={
                        'price': plat['price'],
                        'stock': plat['stock']
                    }
                )
        self.stdout.write(self.style.SUCCESS('Sample books loaded successfully.'))
