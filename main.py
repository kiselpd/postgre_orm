from source.database import DataBaseSession
import json
from source.models import Publisher, Book, Stock, Shop, Sale


def read_json_file(file_name: str)->list:
    db_list = []

    models = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
    }

    with open(file_name) as f:
        for note in json.load(f):
            fields = note.get("fields")
            model = models[note.get("model")]
            db_list.append(model(id=note.get("pk"), **fields))
        
    return db_list
            

def print_shops(shops_list: list):
    for book_title, shop_name, price, date in shops_list:
        print(f"{book_title:40}|{shop_name:10}|{price:10}|{date}")


if __name__=="__main__":

    username = ...
    password = ...
    db_name = ...
    address = ...
    port = ...
    file_name = "test/tests_data.json"

    db_session = DataBaseSession(username, password, db_name)
    db_session.drop_tables() #удалить таблицы(на всякий случай)

    db_session.create_tables() #создать таблицы(задание 1)
    db_session.create_session() #открыть сессию

    db_session.insert_data(read_json_file(file_name)) #вставить данные из файла в БД(задание 3)

    publisher_name = input()
    shop_list = db_session.get_shops_for_publisher(publisher_name) # Запрос выборки магазинов, продающих целевого издателя в БД(задание 2)
    print_shops(shop_list)

    db_session.close_session() #закрыть сессию

    
