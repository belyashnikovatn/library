"""
Model layer.

Serialize and deserialize data, load/save into file.
"""

import json
from typing import Union

BOOKS = [
    {
        'id': 1,
        'title': 'Повелитель мух',
        'author': 'У.Голдинг',
        'year': 1996,
        'status': 'выдана'
    },
    {
        'id': 2,
        'title': 'Смерти.net',
        'author': 'Татьяна Замировская',
        'year': 1996,
        'status': 'выдана'
    },
    {
        'id': 3,
        'title': 'Опосредованно',
        'author': 'А.Сальников',
        'description': 'Альтернативная реальность, где стихи - это не просто текст, а настоящий наркотик',
        'status': 'выдана'
    },
]


def save_json(file_name: str, books: list[dict[str, object]]) -> str:
    """Serialize and save data into json file."""
    data = json.dumps(books, indent=4)
    try:
        with open(file_name, 'w') as outfile:
            outfile.write(data)
        return ('Done!')
    except IOError as e:
        return (f'Error : {e}')


def load_data(file_name) -> Union[list[dict[str, object]], str]:
    """Open file and deserialize data."""
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
        return data
    except IOError as e:
        return f'Error: {e}'


save_json('storage.json', BOOKS)
result = load_data('storage.json')
print(result)
