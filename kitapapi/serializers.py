from rest_framework import serializers
from .models import Book, Platform, Category, BookAvailability

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class BookAvailabilitySerializer(serializers.ModelSerializer):
    platform = PlatformSerializer()
    class Meta:
        model = BookAvailability
        fields = ['platform', 'price', 'stock']

class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    availabilities = BookAvailabilitySerializer(many=True, read_only=True)
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'publisher', 'year', 'category', 'availabilities']
