"""View."""

# from controller import Book
from model import load_data, save_json
from view import get_main_menu, get_list

# result = load_data('storage.json')
# print(result)
# Book('Остров сокровищ', 'Стивенсон', '1888')
# Book('Маша и медведи', 'Народные сказки', '1905')
# Book('Пример', 'Автор', '1905', id=5)
# Book.get_all()
# save_json(Book.library)
# Book.clean()
# Book.get_all()

# if result := load_data():
#     [Book(*book) for book in result]
#     Book.get_all()
# else:
#     print('That case')
#     Book.get_all()


menu_actions = {
    'с': get_list,
    'в': get_main_menu,
    # 'д': Book,
    # 'у': Book.delete,
    # 'и': Book.change_status,
    # 'п': Book.search_by_param,
    'х': ''
}


while True:
    user_input = get_main_menu()
    menu_actions[user_input]()
