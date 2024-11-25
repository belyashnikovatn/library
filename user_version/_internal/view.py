"""
Interface level.

Menus for actions: user pick a menu, make an action, see results.
"""

from controller import Book
from model import save_json
from settings import AUTHOR_ALLOW, MAX_YEAR, MIN_YEAR


def check_value(pattern: list, value: str) -> bool:
    """Check input value."""
    return all([item.lower() in pattern for item in value])


def check_menu(menu: dict) -> str:
    """Check if user's picked a item of a menu."""
    while True:
        [print(f'[ {item[0]} = {item[1]}', end=' ] ') for index, item
            in enumerate(menu.items()) if index < len(menu) // 2]
        print()
        [print(f'[ {item[0]} = {item[1]}', end=' ] ') for index, item
            in enumerate(menu.items()) if index >= len(menu) // 2]
        print()
        user_input = input('Выберите пункт меню: ')
        if user_input in menu:
            return user_input


def get_main_menu() -> str:
    """Get main menu and return the answer."""
    menu = {
        'в': 'список всех книг',
        'к': 'поиск по книгам',
        'т': 'сортировать книги',
        'д': 'добавить книгу',
        'и': 'изменить статус книги',
        'л': 'удалить книгу',
        'й': 'выйти',
    }
    return check_menu(menu)


def get_list() -> None:
    """Get a library."""
    Book.get_all()


def add_book() -> None:
    """Check inputs & add a book."""
    while True:
        author = input('Введите автора: ')
        if check_value(AUTHOR_ALLOW, author):
            break
        print('Допустимы только буквы и знаки .,-')
    title = input('Введите наименование: ')
    while True:
        year = input('Введите год: ')
        if year.isnumeric() and MIN_YEAR < int(year) <= MAX_YEAR:
            year = int(year)
            break
        print(f'Год должен быть числом в диапазоне {MIN_YEAR} - {MAX_YEAR}')
    book = Book(title, author, year)
    print(f'Книга под № {book.id} добавлена!')


def edit_book() -> None:
    """Check input type and edit a book."""
    while True:
        id = input('Введите номер книги: ')
        if id.isnumeric():
            id = int(id)
            break
        print('Введите число!')
    if not Book.get_by_id(id):
        print(f'Нет книги под номером {id}.')
        return
    status = input(
        f'Введите статус из возможных: {", ".join(Book.statuses)}: '
    )
    Book.change_status(id, status)


def del_book() -> None:
    """Check input type and delete a book."""
    while True:
        id = input('Введите номер книги: ')
        if id.isnumeric():
            id = int(id)
            break
        print('Введите число!')
    if not Book.get_by_id(id):
        print(f'Нет книги под номером {id}.')
    if Book.delete(id):
        print(f'Книга под номером {id} удалена.')


def search_book() -> None:
    """Search books by parameters."""
    atr = input(f'Введите поле для поиска [{", ".join(Book.search_fields)}]: ')
    text = input('Что ищем? (например "Пушкин", "выдана", "2005"): ')
    Book.search_by_param(atr, text)


def sort_book() -> None:
    """Sort books by parameters."""
    atr = input(f'Введите поле сортировки [{", ".join(Book.sort_fields)}]: ')
    by = input(f'По возрастанию или убыванию: {", ".join(Book.sort_by)}: ')
    Book.sort_by_param(atr, by)


def get_quit() -> None:
    """Save data into file and say bye."""
    save_json(Book.library)
    print('Данные сохранены. До встречи!')
    quit()
