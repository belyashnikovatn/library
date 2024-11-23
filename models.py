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
            id: int = 0,
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
        """Find max id and return next."""
        if not Book.library:
            return 1
        return max([book.id for book in Book.library]) + 1

    @classmethod
    def _get_by_id(cls, id) -> Union[object, None]:
        """Find a book by id."""
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
    def change_status(cls, id: int, status: str) -> None:
        """Change a book status."""
        book = Book._get_by_id(id)
        if not book:
            print(f'Нет книги под номером {id}.')
            return None
        if not status.lower() in [item.value.lower() for item in BookStatus]:
            print(f'Статуса "{status}" нет.')
            return None
        if status.lower() == book.status.value.lower():
            print(f'У книги под номером {id} уже статус "{status}"')
            return None
        new_status = [item for item in BookStatus if item.value.lower() == status.lower()][0]
        book.status = new_status
        print(f'Книга под номером {id} теперь "{book.status.value}"')


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


# Book.get_all()
# Book('Сказки', 'Гоголь', 1952)
# Book('Роман', 'Толстой', 1934)
# Book('Стихи', 'Пушкин', 1934)

# Book.get_all()
# Book.delete(2)
# Book.get_all()
# Book.delete(6)

# Book('Поэма', 'Блок', 1917)

# Book.get_all()
# print('-------------')
# Book.get_all_by_param(author='Гоголь')
# Book.get_all_by_param(author='Г1231оголь')

test_book = Book('SinnSongs', 'People', 1212)
Book.change_status(1, 'ДРУГОЙ')
Book.change_status(1, 'в наличии')
Book.change_status(1, 'ВЫДАНа')
Book.get_all()
# print([item.value for item in BookStatus])
# print([item.name for item in BookStatus])
# def some_function(value: str):
#     try:
#         value_atr = getattr(test_book, value)
#         print (value_atr)
#     except AttributeError as e:
#         print(f'This is {e} error')


# some_function("title")
# some_function("title123")