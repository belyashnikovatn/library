"""
Interface level.

Menus for actions: user pick a menu, make an action, see results.
"""

from controller import Book
from model import load_data, save_json


def check_menu(menu: dict) -> str:
    """Check if user's picked a item of a menu."""
    while True:
        [print(f'{item[0]} -> {item[1]}') for item in menu.items()]
        user_input = input('Выберите пункт меню: ')
        if user_input in menu:
            return user_input


def get_main_menu() -> str:
    """Get main menu and return the answer."""
    menu = {
        'в': 'список всех книг',
        'п': 'поиск по книгам',
        'д': 'добавить книгу',
        'и': 'изменить статус книги',
        'у': 'удалить книгу',
        'х': 'выйти',
    }
    return check_menu(menu)


def get_list():
    """Get a library and functions."""
    if result := load_data():
        [Book(*book) for book in result]
    Book.get_all()
    get_main_menu()


def add_book():
    author = input('Введите автора: ')
    title = input('Введите наименование: ')
    year = input('Введите год: ')
    book = Book(title, author, year)
    print(f'Книга под № {book.id} сохранена!')
    get_main_menu()


def edit_book():
    id = int(input('Введите номер книги: '))
    status = input(
        f'Введите статус из возможных: {", ".join([s for s in Book.statuses])}'
    )
    Book.change_status(id, status)
    get_main_menu()


def del_book():
    id = int(input('Введите номер книги: '))
    Book.delete(id)
    get_main_menu()


def search_book():
    atr = input('Введите поле для поиска (например "автор"): ')
    text = input('Введите текст поиска (например "Пушкин"): ')
    Book.search_by_param(atr, text)
    get_main_menu()


def get_quit() -> bool:
    """Save data into file and say bye."""
    save_json(Book.library)
    print('Данные сохранены. До встречи!')
    quit()
