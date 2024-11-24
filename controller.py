"""
Controller layer.

All CRUD operations for books: add, delete, change a status, get a list;
additional: search by parameters, sort by parameters.
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
        'год': 'year'
    }

    # Fields for sorting: you can add more:
    sort_fields = {
        'автор': 'author',
        'наименование': 'title'
    }
    # Sorting direction:
    sort_by = {
        'в': True,
        'у': False
    }

    def __init__(
            self, title: str, author: str, year: str,
            id: int = 0,
            status: str = statuses[0]
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
        """Find a book by id and return an instance (or None)."""
        if result := [book for book in Book.library if book.id == id]:
            return result[0]
        return None

    @classmethod
    def delete(cls, id: int) -> None:
        """Delete a book by id."""
        book = Book._get_by_id(id)
        if book:
            Book.library.remove(book)
            print(f'Книга под номером {id} удалена.')
            return None
        print(f'Нет книги под номером {id}.')

    @classmethod
    def change_status(cls, id: int, status: str) -> None:
        """Change a book status by id."""
        book = Book._get_by_id(id)
        if not book:
            print(f'Нет книги под номером {id}.')
            return None
        if not status.lower() in cls.statuses:
            print(f'Статуса "{status}" нет.')
            return None
        if status.lower() == book.status.lower():
            print(f'У книги под номером {id} уже статус "{status}"')
            return None
        book.status = status.lower()
        print(f'Книга под номером {id} теперь "{book.status}"')

    @classmethod
    def get_all(cls) -> None:
        """Print a list of all books."""
        if results := [book for book in Book.library]:
            print(f'Библиотека. Всего  книг: {len(results)}')
            [print(book) for book in results]
            print('---')
            return None
        print('Библиотека пустая. Сначала добавьте в неё что-нибудь.')

    @classmethod
    def search_by_param(
        cls, atr, text
    ) -> None:
        """Print a list of all books by parameter."""
        if atr.lower() not in cls.search_fields:
            print(f'Поля "{atr}" нет. Попробуйте ещё раз')
            return None
        if results := [book for book in Book.library if getattr(book, cls.search_fields[atr]).lower() == text.lower()]:
            print(f'Результаты поиска по полю "{atr}" по значению "{text}":')
            [print(book) for book in results]
            print(f'--- найдено всего {len(results)} ---')
            return None
        print(f'По полю "{atr}" по значению "{text}" ничего не найдено.')

    @classmethod
    def sort_by_param(cls, atr, by) -> None:
        """Print a list of all books sorted by parameter."""
        if atr.lower() not in cls.sort_fields:
            print(f'Поля {atr} нет. Попробуйте ещё раз.')
            return None
        if by.lower() not in cls.sort_by:
            print(f'Аргумента {by} нет. Попробуйте ещё раз.')
            return None
        if results := sorted(Book.library, key=lambda x: getattr(x, cls.sort_fields[atr]).lower(), reverse=cls.sort_by[by]):
            print(f'Книги отсортированы по полю "{atr}" по "{by}":')
            [print(book) for book in results]
            print('---')
        print('Библиотека пустая. Сначала добавьте в неё что-нибудь.')

    def __str__(self):
        """Return full description of a book."""
        return (
            f'Книга номер {self.id}: '
            f'под названием "{self.title}" авторства {self.author}, '
            f'{self.year} года выпуска сейчас {self.status}')


# Book('Сказки', 'Гоголь', '1952')
# Book.get_all_by_param(atr='author', text='test')
Book.get_all()
Book('Сказки', 'Гоголь', '1952')
Book('Роман', 'Толстой', '1934')
Book('Стихи', 'Пушкин', '1934')

Book.get_all()
Book.sort_by_param('автоывур', 'в')
Book.sort_by_param('автор', '23123')
Book.sort_by_param('наименование', 'в')
Book.sort_by_param('наименование', 'у')
Book.sort_by_param('автор', 'у')
# Book.get_all_by_param(atr='автор', text='test')
# Book.get_all_by_param(atr='год', text='1934')
# Book.get_all_by_param(atr='автор', text='гоголь')
# Book.delete(2)
# Book.get_all()
# Book.delete(6)

# Book('Поэма', 'Блок', 1917)

# Book.get_all()
# print('-------------')
# Book.get_all_by_param(author='Гоголь')
# Book.get_all_by_param(author='Г1231оголь')

# test_book = Book('SinnSongs', 'People', 1212)
# Book.change_status(1, 'ДРУГОЙ')
# Book.change_status(1, 'в наличии')
# Book.change_status(1, 'ВЫДАНа')
# Book.get_all()
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