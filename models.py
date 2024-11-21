"""All CRUD-operations for books."""

from enum import Enum


class BookStatus(Enum):
    """Desc."""

    IN_STOCK = 'в наличии'
    ABSENT = 'выдана'


class Book():
    """Book class."""

    library: list[object] = []

    def __init__(
            self, id: int, title: str, author: str, year: int,
            status: BookStatus = BookStatus.IN_STOCK
    ) -> None:
        """Initialize a book and add into library."""
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

        Book.library.append(self)

    @classmethod
    def get_all(cls):
        """Return a list of all books."""
        return [book for book in Book.library]

    def __str__(self):
        """Return full description of a book."""
        return (
            f'Книга номер {self.id}: '
            f'под названием "{self.title}" авторства {self.author}, '
            f'{self.year} года выпуска сейчас {self.status.value}')


book = Book(1, 'Сказки', 'Гоголь', 1952)
book = Book(2, 'Роман', 'Толстой', 1934)
[print(book) for book in Book.get_all()]