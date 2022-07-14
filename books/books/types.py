from dataclasses import dataclass
from datetime import datetime


@dataclass
class BookAuthors:
    id: str
    book_id: str
    authors: List[str]


@dataclass
class BookRatings:
    id: str
    book_id: str
    user_id_to_rating: Dict[str, int]  # {"user1": 4, "user2": 5}

    @property
    def average_ratings(self):
        avg_rating = sum(v for k, v in self.user_id_to_rating.items()) / len(
            self.user_id_to_rating
        )
        return avg_rating


class BookAvailbility:
    book_id: str
    available_copies: int


class BookPrice:
    book_id: str
    cost_in_cents: int


@dataclass
class BookDetails:
    book_id: str
    title: str
    isbn: str
    published_date: datetime.Date
    book_author: BookAuthors
    book_price: BookPrice
    book_avalabilty: BookAvailbility
    book_ratings: BookRatings

    @property
    def number_of_days_from_published(self):
        return datetime.today.date() - self.published_date

    @property
    def books_available(self):
        return self.book_availability.available_copies

    @property
    def book_name(self):
        return self.title

    @property
    def published_year(self):
        return self.published_date.year()
