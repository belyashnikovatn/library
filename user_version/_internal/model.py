"""
Model layer.

Serialize and deserialize data, load/save into file.
"""

import json
from pathlib import Path
from typing import Union

from settings import logging, STORAGE


def save_json(books: list[object], file_name: str = STORAGE) -> None:
    """Serialize and save data into json file."""
    data = json.dumps([book.dump() for book in books], indent=4)
    try:
        with open(file_name, 'w') as outfile:
            outfile.write(data)
        logging.debug('Данные успешно сохранены в файл')
    except IOError as e:
        logging.error(f'Ошибка : {e}')


def load_data(file_name: str = STORAGE) -> Union[list[list], None]:
    """Open file and deserialize data."""
    if not Path(file_name).is_file():
        logging.debug(f'Файл {STORAGE} не существует')
        return None
    try:
        with open(file_name, 'r') as file:
            try:
                data = json.load(file)
                return data
            except ValueError as e:
                logging.error(f'Ошибка: {e}')
                return None
    except IOError as e:
        logging.error(f'Ошибка: {e}')
        return None
