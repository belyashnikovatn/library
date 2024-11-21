import os


STORAGE_NAME = 'library'
STORAGE_FORMAT = '.json'
STORAGE_PATH = ''.join([os.getcwd(), STORAGE_NAME, STORAGE_FORMAT])

print(STORAGE_PATH)
