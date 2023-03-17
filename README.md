# Домашнее задание к лекции «Python и БД. ORM»

![](readme_зтп/book_publishers_scheme.png)

## *source/database.py* - модуль для работы с БД
```
class DataBaseSession:
    
    def __init__(self, username: str, password: str, db_name: str, address: str="localhost", port: str="5432") -> инитиализация подключения к БД

    def create_session(self) -> открытие сессии

    def close_session(self) -> закрытие сессии


    def create_tables(self) -> создание таблиц

    
    def drop_tables(self) -> удаление таблиц

    
    def insert_data(self, data_list: list) -> вставка данных

    
    def get_shops_for_publisher(self, name_publisher: str) -> получить список продаж определенного издателя (Задание 2)
```

## *source/models.py* - модуль c моделями таблиц в БД
```
Задание 1:

    Base = declarative_base()

    class Publisher(Base):
        ...

    class Book(Base):
        ...

    class Shop(Base)
        ...

    class Stock(Base):
        ...

    class Sale(Base):
        ...
```

## *main.py* - основной файл
```
def read_json_file(file_name: str) -> чтение из json-файла в БД(Задание 3

def print_shops(shops_list: list) -> форматированный вывод для Задания 2
```