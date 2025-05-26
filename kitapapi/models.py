from django.db import models

class Platform(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=20, unique=True)
    publisher = models.CharField(max_length=255)
    year = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

class BookAvailability(models.Model):
    book = models.ForeignKey(Book, related_name='availabilities', on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    price = models.FloatField()
    stock = models.BooleanField()

    def __str__(self):
        return f"{self.book.title} - {self.platform.name}"

