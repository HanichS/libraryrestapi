from .models import BookLend
from datetime import datetime


# Business rules for BookLends
class BookLendService:

    fine_rate = {
        0: 0.0,
        3: 0.03,
        5: 0.05,
        6: 0.07
    }

    daily_interest_rate = {
        0: 0.0,
        3: 0.002,
        5: 0.004,
        6: 0.006
    }

    @staticmethod
    def is_lent(book_id):
        return len(BookLend.objects.filter(book_id=book_id, return_date__isnull=True))

    @classmethod
    def calculate_lend_fine_interest(cls, book):
        lend = BookLend.objects.filter(book=book, return_date__isnull=True)
        lend = lend[0]
        print(datetime.today().date())
        delta = datetime.today().date() - lend.lend_date
        days_late = delta.days - 3
        rate = cls.__get_rate(days_late)

        return cls.__sum_fine_plus_interest(rate, book.lend_price, days_late)

    @classmethod
    def __get_rate(cls, days_late):
        if days_late <= 0:
            return 0
        if days_late <= 3:
            return 3
        if days_late <= 5:
            return 5

        return 6

    @classmethod
    def __sum_fine_plus_interest(cls, rate, lend_price, days_late):
        total_fine = float(lend_price) * cls.fine_rate[rate]
        total_interest = float(lend_price) * cls.daily_interest_rate[rate] * days_late
        return total_fine + total_interest







