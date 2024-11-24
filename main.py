"""View."""

from controller import Book
from model import load_data, save_json

# result = load_data('storage.json')
# print(result)
Book('Остров сокровищ', 'Стивенсон', '1888')
Book('Маша и медведи', 'Народные сказки', '1905')
Book('Пример', 'Автор', '1905', id=5)
Book.get_all()
save_json(Book.library)
Book.clean()
Book.get_all()
result = load_data()
if result:
    [Book(*book) for book in result]
    Book.get_all()
else:
    print('That case')
    Book.get_all()
    
# print(result)
