"""Model layer: save data into json OR json into structure"""


import uuid

BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'Повелитель мух',
        'author': 'У.Голдинг',
        'year': 1996,
        'status': 'выдана'
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Смерти.net',
        'author': 'Татьяна Замировская',
        'year': 1996,
        'status': 'выдана'
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Опосредованно',
        'author': 'А.Сальников',
        'description': 'Альтернативная реальность, где стихи - это не просто текст, а настоящий наркотик',
        'status': 'выдана'
    },
]
