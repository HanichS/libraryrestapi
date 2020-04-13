from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializers import AuthorSerializer, BookSerializer, BookLendSerializer, BooksWithClientSerializer, ClientSerializer
from .models import Author, Book, Client, BookLend
from rest_framework_extensions.mixins import NestedViewSetMixin


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BooksWithClientViewSet(NestedViewSetMixin, ReadOnlyModelViewSet):
    queryset = Book.objects.filter(booklend__return_date__isnull=True)
    serializer_class = BooksWithClientSerializer


class BookLendViewSet(NestedViewSetMixin, ModelViewSet):
    queryset = BookLend.objects.all()
    serializer_class = BookLendSerializer

    def create(self, request, **kwargs):
        request.data['book_id'] = self.kwargs['parent_lookup_book_id']
        return super(BookLendViewSet, self).create(request, **kwargs)


class BookViewSet(NestedViewSetMixin, ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ClientViewSet(NestedViewSetMixin, ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer



