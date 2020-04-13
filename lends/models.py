from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=150)
    genre = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    lend_price = models.DecimalField(max_digits=5, decimal_places=2, default=5.)

    @property
    def available(self):
        # check if book is not lent
        return not len(BookLend.objects.filter(book=self, return_date__isnull=True))

    def __str__(self):
        return self.title


class Client(models.Model):
    name = models.CharField(max_length=150)
    books_lent = models.ManyToManyField(Book, through='BookLend')

    def __str__(self):
        return self.name


class BookLend(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    lend_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.book.title} to {self.client.name} in {self.lend_date.__str__()}'



