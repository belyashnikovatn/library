"""Main app."""

from controller import Book
from model import load_data
from view import (
    add_book,
    del_book,
    edit_book,
    get_list,
    get_main_menu,
    get_quit,
    search_book,
    sort_book
)


# Dictionary of buttons-functions
menu_actions = {
    'в': get_list,
    'к': search_book,
    'т': sort_book,
    'д': add_book,
    'и': edit_book,
    'л': del_book,
    'й': get_quit
}


if __name__ == '__main__':
    # Load library if it exists.
    if result := load_data():
        [Book(*book) for book in result]
    print('Добро пожаловать в Библиотеку!')
    while True:
        user_input = get_main_menu()
        menu_actions[user_input]()
