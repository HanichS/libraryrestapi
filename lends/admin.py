from django.contrib import admin
from .models import Author, Client, Book, BookLend

# Register your models here.
admin.site.register(Author)
admin.site.register(Client)
admin.site.register(Book)
admin.site.register(BookLend)