"""
Model layer.

Serialize and deserialize data, load/save into file.
"""

import json


def save_json(file_name: str, books: list[object]) -> str:
    """Serialize and save data into json file."""
    data = json.dumps([book.dump() for book in books], indent=4)
    try:
        with open(file_name, 'w') as outfile:
            outfile.write(data)
        return ('Done!')
    except IOError as e:
        return (f'Error : {e}')


def load_data(file_name) -> list[dict]:
    """Open file and deserialize data."""
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
        return data
    except IOError as e:
        return f'Error: {e}'
