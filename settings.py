import logging
from datetime import datetime as dt


logging.basicConfig(
    format='%(asctime)s - %(funcName)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

STORAGE_NAME, STORAGE_FORMAT = 'library', 'json'
STORAGE = '.'.join([STORAGE_NAME, STORAGE_FORMAT])

MIN_YEAR = 1445
MAX_YEAR = dt.now().year
AUTHOR_ALLOW = [chr(i) for i in range(ord('a'), ord('z') + 1)] + [chr(i) for i in range(ord('а'), ord('я') + 1)] + ['ё', '.', ',', '-', ' ']
