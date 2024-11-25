# 📚 Библиотека
## Система управления библиотекой: каждой книге своё место!  
Система реализована в виде консольного приложения, которое позволяет добавлять, удалять, искать, сортировать и отображать книги.  
Проект выполнен в качестве тестового задания для вакансии в «Effective Mobile».

## Функционал:
- [x] Хранение данных о книгах в json формате
- [x] Отображение всех книг: приложение выводит список всех книг
- [x] Поиск книги: пользователь может искать книги по автору, наименованию, году
- [x] Добавление книги: пользователь вводит поля "наименование", "автор", "год", после чего книга добавляется в библиотеку с уникальным id и статусом "в наличии".
- [x] Удаление книги: пользователь вводит id книги, которую нужно удалить.
- [x] Изменение статуса книги: пользователь вводит id книги и новый статус ("в наличии", "выдана")
- [x] Сортировка книг: пользователь может отсортировать книги по автору, наименованию, году  


Дополнительные требования
-  Обеспечить корректную обработку ошибок (например, попытка удалить
несуществующую книгу). На многих уровнях
- Не использовать сторонние библиотеки.

Критерии оценки:
- Корректность и полнота реализации функционала.
- Чистота и читаемость кода.
- Обработка ошибок и исключений.
- Удобство использования интерфейса командной строки.
- Структура проекта.
- Насйтроки : путь + имя файла .
- Test int year 

расщиряемомсть в списках поиска и сортировки  
в вплане интерфейса

## Установка:
```
$ git clone https://github.com/belyashnikovatn/library.git
$ python main.py
```

## Стек и реализация:
python 3.9 + только внутренние модули (согласно ТЗ). Приложение реализовано по паттерну MVC.

### Уровень представления
Точка входа в программу реализована в файле main.py в словаре menu_actions вида "опция" - "функция". Пользователь ограничен интерфейсом и может выбрать из заданного меню только букву. Буквы выбраны так, чтобы было понятно, что это точно русскоязычная раскладка (чтобы не путать и не переключаться зря). Представления реализованы в view.py: отрисовка меню, проверка введённых пользователем данных, вызов методов класса Book. Для проверки некоторых значений заданы константы, которые находятся в settings.py. Меню с опциями и функциями можно расширять: отрисовка делит меню на 2 строчки пополам.

### Уровень логики
Для работы с книгами реализован класс Book в файле controller.py. Работа с коллекцией книг реализована на уровне класса. Методы разделены на внутренние и внешние; на методы класса и методы экземпляра. Для поиска и сортировки предусмотрены справочники на уровне класса: statuses, search_fields, sort_fields, sort_by. Получение id реализовано в методе _get_next_id. Также реализованы проверки при удалении, измененении, поиске, сортировке. Добавление книги происходит при инициализации объекта класса (создание объекта, добавление в список) и предусмтаривает варианты добавления с id (при загрузке из файла) и без него (для создания из интерфейса). 

### Уровень данных
При запуске программы происходит чтение из файла формата json. При окончании работы с программой происходит запись в тот же файл. Имя и тип файла хранятся в settings.py (для расширения функционала хранения и/или для реализации функции выбора настроек). Чтение и запись в файл реализованы в файле model.py с помощью json модуля. Для сохранения объектов класса Book в json-формат используется метод класса dump. При попытке открыть файл и считать из него данные, происходят проверки на существование файла, на его пустоту, на возможность считывания данных. Подключено логирование, уровень можно поменять в settings (сейчас выставлено на уровень INFO).


## Дополнительно

### Обработка ошибок и исключений
Реализована проверка типов и возможные варианты данных. Видимость ошибко зависит от уровня и возможности исправления: ошибки, на которые пользователь может повлиять, выводятся на экран, а ошибки, которые зависят не от него, пишутся в логи.

### Примеры работы программы

