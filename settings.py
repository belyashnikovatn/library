import logging

logging.basicConfig(
    format='%(asctime)s - %(funcName)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

STORAGE_NAME, STORAGE_FORMAT = 'library', 'json'
STORAGE = '.'.join([STORAGE_NAME, STORAGE_FORMAT])
