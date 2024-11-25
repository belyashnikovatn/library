"""Main app."""

from view import (
    add_book,
    del_book,
    edit_book,
    get_main_menu,
    get_list,
    get_quit,
    search_book
)


menu_actions = {
    'в': get_list,
    'п': search_book,
    'д': add_book,
    'и': edit_book,
    'у': del_book,
    # 'о': ,
    'х': get_quit
}


while True:
    user_input = get_main_menu()
    menu_actions[user_input]()
