"""All CRUD-operations for books."""

from enum import Enum


class BookStatus(Enum):
    """Desc."""

    IN_STOCK = 'в наличии'
    ABSENT = 'выдана'


class Book:
    """Book class."""

    def __init__(
            self, id: int, title: str, author: str, year: int,
            status: BookStatus = BookStatus.IN_STOCK
    ) -> None:
        """Initialize an instance of a book."""
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status


book = Book(1, 'Сказки', 'Гоголь', 1952)
print(f'Книга номер {book.id} = {book.title, book.author, book.year, book.status.value}')
