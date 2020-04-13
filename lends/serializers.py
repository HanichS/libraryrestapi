from rest_framework import serializers
from .models import Book, Client, Author, BookLend
from .services import BookLendService
from django.core.exceptions import ValidationError


# Used in /client/{id}/books, adds fine and interest info
class BooksWithClientSerializer(serializers.ModelSerializer):
    fine_plus_interest = serializers.SerializerMethodField('get_fine_plus_interest')

    def get_fine_plus_interest(self, obj):
        return BookLendService.calculate_lend_fine_interest(obj)

    class Meta:
        model = Book
        fields = ('id', 'isbn', 'title', 'genre', 'author', 'lend_price', 'fine_plus_interest')


# Used in /books/{id}/reserve
class BookLendSerializer(serializers.ModelSerializer):
    def validate(self, data):
        request_data = self.context['request'].data
        if BookLendService.is_lent(request_data['book_id']):
            raise ValidationError("Requested book does not exist or is already lent")
        return {'book_id': request_data['book_id'], 'client_id': request_data['client_id']}

    class Meta:
        model = BookLend
        fields = ('id', 'book_id', 'client_id')


# Default Author model serializer, basic CRUD
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name')


# Default Book model serializer, basic CRUD
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'isbn', 'title', 'genre', 'author', 'available', 'lend_price')


# Default Client model serializer, basic CRUD
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name')