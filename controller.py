"""
Controller layer.

All CRUD operations for books: add, delete, change a status, get a list.
Additional operations for collection: search by parameters, sort by parameters.
"""

from typing import Union


class Book:
    """Book class."""

    # Library: list of books inside of the Book class.
    library: list[object] = []

    # Book status scheme: you can add more.
    statuses = ('в наличии', 'выдана')

    # Fields for seraching: you can add more.
    search_fields = {
        'автор': 'author',
        'наименование': 'title',
        'год': 'year',
        'статус': 'status'
    }

    # Fields for sorting: you can add more:
    sort_fields = {
        'автор': 'author',
        'наименование': 'title',
        'статус': 'status'
    }
    # Sorting direction:
    sort_by = {
        'в': True,
        'у': False
    }

    def __init__(
            self, title: str, author: str,
            year: int, id: int = 0,
            status: str = statuses[0]
    ) -> None:
        """Initialize a book and add into the library."""
        self.title = title
        self.author = author
        self.year = year
        self.status = status
        if id in [book.id for book in Book.library] or id == 0:
            self.id = Book._get_next_id()
        else:
            self.id = id
        Book.library.append(self)

    @classmethod
    def _get_next_id(cls) -> int:
        """Find max id and return next."""
        if not Book.library:
            return 1
        return max([book.id for book in Book.library]) + 1

    @classmethod
    def get_by_id(cls, id) -> Union[object, None]:
        """Find a book by id and return an instance (or None)."""
        if result := [book for book in Book.library if book.id == id]:
            return result[0]
        return None

    @classmethod
    def delete(cls, id: int) -> Union[int, None]:
        """Delete a book by id."""
        book = Book.get_by_id(id)
        if book:
            Book.library.remove(book)
            return id
        return None

    @classmethod
    def change_status(cls, id: int, status: str) -> None:
        """Change a book status by id."""
        book = Book.get_by_id(id)
        if not status.lower() in cls.statuses:
            print(f'Статуса "{status}" нет.')
            return
        if status.lower() == book.status.lower():
            print(f'У книги под номером {id} уже статус "{status}"')
            return
        book.status = status.lower()
        print(f'Книга под номером {id} теперь "{book.status}"')

    @classmethod
    def get_all(cls) -> None:
        """Print a list of all books."""
        if results := [book for book in Book.library]:
            print(f'Список книг. Всего: {len(results)}')
            [print(book) for book in results]
            print('---')
            return
        print('Библиотека пустая. Сначала добавьте в неё что-нибудь.')

    @classmethod
    def search_by_param(cls, atr: str, text: str) -> None:
        """Print a list of all books by parameter."""
        if atr.lower() not in cls.search_fields:
            print(f'Поле "{atr}" не доступно для поиска. Попробуйте иначе.')
            return
        if results := [book for book in Book.library if getattr(book, cls.search_fields[atr]).lower() == text.lower()]:
            print(f'Результаты поиска по полю "{atr}" по значению "{text}":')
            [print(book) for book in results]
            print(f'--- найдено всего {len(results)} ---')
            return
        print(f'По полю "{atr}" по значению "{text}" ничего не найдено.')

    @classmethod
    def sort_by_param(cls, atr: str, by: str) -> None:
        """Print a list of all books sorted by parameter."""
        if atr.lower() not in cls.sort_fields:
            print(f'Поле {atr} не доступно для сортировки. Попробуйте иначе.')
            return
        if by.lower() not in cls.sort_by:
            print(f'Аргумента {by} нет. Попробуйте иначе.')
            return
        if results := sorted(Book.library, key=lambda x: getattr(x, cls.sort_fields[atr]).lower(), reverse=cls.sort_by[by]):
            print(f'Книги отсортированы по полю "{atr}" по "{by}":')
            [print(book) for book in results]
            print('---')
            return
        print('Библиотека пустая. Сначала добавьте в неё что-нибудь.')

    def dump(self) -> tuple:
        """Return a dict for serializing."""
        return (self.title, self.author, self.year, self.id, self.status)

    @classmethod
    def clean(cls) -> None:
        """Remove all books: for testing or extension."""
        Book.library.clear()

    def __str__(self) -> str:
        """Return full description of a book."""
        return (
            f'№ {self.id}: '
            f'"{self.title}" авторства "{self.author}", '
            f'{self.year} года выпуска сейчас {self.status}')
