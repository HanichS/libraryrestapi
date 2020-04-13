from rest_framework.routers import DefaultRouter
from lends.viewsets import AuthorViewSet, BookViewSet, BookLendViewSet, BooksWithClientViewSet, ClientViewSet
from rest_framework_extensions.routers import NestedRouterMixin


class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass


router = NestedDefaultRouter()

# /books and /books/{id}/reserve
router.register('books', BookViewSet).register(
    'reserve',
    BookLendViewSet,
    'reserve-books',
    parents_query_lookups=['book_id']
)

# /authors
router.register('authors', AuthorViewSet)

# /client and /client/{id}/books
router.register('client', ClientViewSet).register(
    'books',
    BooksWithClientViewSet,
    'client-books',
    parents_query_lookups=['client'])


    

