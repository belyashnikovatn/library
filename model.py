"""
Model layer.

Serialize and deserialize data, load/save into file.
"""

import json

from settings import logging


def save_json(file_name: str, books: list[object]) -> None:
    """Serialize and save data into json file."""
    data = json.dumps([book.dump() for book in books], indent=4)
    try:
        with open(file_name, 'w') as outfile:
            outfile.write(data)
        logging.info('Данные успешно сохранены в файл')
    except IOError as e:
        logging.error(f'Ошибка : {e}')


def load_data(file_name) -> list[list]:
    """Open file and deserialize data."""
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
        return data
    except IOError as e:
        logging.error(f'Ошибка: {e}')
