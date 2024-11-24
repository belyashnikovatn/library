"""

"""

from controller import Book


def check_menu(menu: dict) -> str:
    """Check if user's picked a item of a menu."""
    while True:
        [print(f'{item[0]} -> {item[1]}') for item in menu.items()]
        user_input = input('Выберите пункт меню: ')
        if user_input in menu:
            return user_input


def get_list() -> str:
    menu = {
        'о': 'отсортировать',
        'п': 'поиск по книгам',
        'в': 'вернуться в главное меню',
    }
    Book.get_all()
    return check_menu(menu)


def get_main_menu() -> str:
    """Get main menu and return the answer."""
    main_menu = {
        'с': 'список всех книг',
        'д': 'добавить книгу',
        'у': 'удалить книгу',
        'и': 'изменить статус книги',
        'п': 'поиск по книгам',
        'х': 'выйти',
    }
    return check_menu(main_menu)
