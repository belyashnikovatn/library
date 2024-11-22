"""All CRUD-operations for books."""

from datetime import datetime as dt
from enum import Enum
from typing import Type, Union


class BookStatus(Enum):
    """Status scheme for books."""

    IN_STOCK = 'в наличии'
    ABSENT = 'выдана'


class Book:
    """Book class."""

    library: list[object] = []

    def __init__(
            self, title: str, author: str, year: int,
            id: int = None,
            status: BookStatus = BookStatus.IN_STOCK
    ) -> None:
        """Initialize a book and add into the library."""
        self.title = title
        self.author = author
        self.year = year
        self.status = status
        if id:
            self.id = id
        else:
            self.id = Book._get_next_id()
        Book.library.append(self)
        print(f'Книга {self.title} успешно добавлена!')

    @classmethod
    def _get_next_id(cls) -> int:
        """Internal method: find max id and return next."""
        if not Book.library:
            return 1
        return max([book.id for book in Book.library]) + 1

    @classmethod
    def _get_by_id(cls, id) -> Union[object, None]:
        """Internal method: find a book by id."""
        if result := [book for book in Book.library if book.id == id]:
            return result[0]
        return None

    @classmethod
    def get_all(cls) -> None:
        """Return a list of all books or None."""
        if result := [book for book in Book.library]:
            [print(book) for book in result]
        else:
            print('Библиотека пустая. Сначала добавьте в неё что-нибудь.')

    @classmethod
    def delete(cls, id):
        """Delete a book by id."""
        book = Book._get_by_id(id)
        if book:
            Book.library.remove(book)
            print(f'Книга под номером {id} удалена.')
        else:
            print(f'Нет книги под номером {id}.')

    @classmethod
    def get_all_by_param(
        # self, atr, text
        cls, author: str = '', title: str = '',
        year: int = dt.now().year
    ):
        """Return a list of all books by parameters."""
        if author:
            result = [book for book in Book.library if book.author.lower() == author.lower()]
        if result:
            print(f'Реузльтаты поиска по {author}')
            [print(book) for book in result]
        else:
            print(
                f'По запросу {author} ничего не найдено'
                '. Попробуйте по-другому')

    def __str__(self):
        """Return full description of a book."""
        return (
            f'Книга номер {self.id}: '
            f'под названием "{self.title}" авторства {self.author}, '
            f'{self.year} года выпуска сейчас {self.status.value}')


Book.get_all()
Book('Сказки', 'Гоголь', 1952)
Book('Роман', 'Толстой', 1934)
Book('Стихи', 'Пушкин', 1934)

Book.get_all()
Book.delete(2)
Book.get_all()
Book.delete(6)

Book('Поэма', 'Блок', 1917)

Book.get_all()
print('-------------')
Book.get_all_by_param(author='Гоголь')
Book.get_all_by_param(author='Г1231оголь')

# test_book = Book()
# def some_function(value: str):
#     return getattr(Book, value)


# print(some_function(""))