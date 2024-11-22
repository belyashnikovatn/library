"""All CRUD-operations for books."""

from enum import Enum


class BookStatus(Enum):
    """Status scheme for books."""

    IN_STOCK = 'в наличии'
    ABSENT = 'выдана'


class Book():
    """Book class."""

    library: list[object] = []

    def __init__(
            self, title: str, author: str, year: int,
            id: int = 0,
            status: BookStatus = BookStatus.IN_STOCK
    ) -> None:
        """Initialize a book and add into the library."""
        self.id = Book._get_next_id()
        self.title = title
        self.author = author
        self.year = year
        self.status = status

        Book.library.append(self)

    @classmethod
    def _get_next_id(cls):
        """Find max id and return next."""
        if not Book.library:
            return 1
        return max([book.id for book in Book.library]) + 1

    @classmethod
    def get_all(cls):
        """Return a list of all books."""
        return [book for book in Book.library]

    @classmethod
    def _get_by_id(cls, id):
        """Internal method: find a book by id."""
        return [book for book in Book.library if book.id == id][0]

    @classmethod
    def delete(cls, id):
        """Delete a book by id."""
        book = Book._get_by_id(id)
        Book.library.remove(book)

    def __str__(self):
        """Return full description of a book."""
        return (
            f'Книга номер {self.id}: '
            f'под названием "{self.title}" авторства {self.author}, '
            f'{self.year} года выпуска сейчас {self.status.value}')


book = Book('Сказки', 'Гоголь', 1952)
book = Book('Роман', 'Толстой', 1934)
book = Book('Стихи', 'Пушкин', 1934)
book = Book('Поэма', 'Блок', 1917)

[print(book) for book in Book.get_all()]

# found = Book.get_by_id(2)
# found = Book.get_by_id(1)
# print(found)
print('==============')
Book.delete(2)
[print(book) for book in Book.get_all()]

