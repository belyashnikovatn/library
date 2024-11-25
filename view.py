"""
Interface level.

Menus for actions: user pick a menu, make an action, see results.
"""


from controller import Book
from model import save_json
from settings import MAX_YEAR, MIN_YEAR

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


def get_list():
    """Get a library."""
    Book.get_all()


def add_book():
    """Add a book."""
    author = input('Введите автора: ')
    title = input('Введите наименование: ')
    while True:
        year = input('Введите год: ')
        if year.isnumeric() and MIN_YEAR < int(year) <= MAX_YEAR:
            break
        print(f'Год должен быть числом в диапазоне {MIN_YEAR} - {MAX_YEAR}')
    book = Book(title, author, year)
    print(f'Книга под № {book.id} сохранена!')


def edit_book():
    id = int(input('Введите номер книги: '))
    status = input(
        f'Введите статус из возможных: {", ".join(Book.statuses)}: '
    )
    Book.change_status(id, status)


def del_book():
    id = int(input('Введите номер книги: '))
    Book.delete(id)


def search_book():
    atr = input(f'Введите поле для поиска [{", ".join(Book.search_fields)}]: ')
    text = input('Введите текст поиска (например "Пушкин", "выдана", "2005"): ')
    Book.search_by_param(atr, text)


def sort_book():
    atr = input(f'Введите поле сортировки [{", ".join(Book.sort_fields)}]: ')
    by = input(f'По возрастанию или убыванию: {", ".join(Book.sort_by)}: ')
    Book.sort_by_param(atr, by)


def get_quit() -> None:
    """Save data into file and say bye."""
    save_json(Book.library)
    print('Данные сохранены. До встречи!')
    quit()
