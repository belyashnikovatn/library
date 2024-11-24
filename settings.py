import logging
import os

logging.basicConfig(
    format='%(asctime)s - %(funcName)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

STORAGE_NAME = 'library'
STORAGE_FORMAT = '.json'
STORAGE_PATH = ''.join([os.getcwd(), STORAGE_NAME, STORAGE_FORMAT])

print(STORAGE_PATH)
