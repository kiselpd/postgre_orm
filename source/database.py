import sqlalchemy
from sqlalchemy.orm import sessionmaker
from .models import Base, Publisher, Book, Stock, Sale, Shop


class DataBaseSession:
    
    def __init__(self, username: str, password: str, db_name: str, address: str="localhost", port: str="5432"):
        DSN = f'postgresql://{username}:{password}@{address}:{port}/{db_name}'
        self.__engine = sqlalchemy.create_engine(DSN)


    def create_session(self):
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()


    def close_session(self):
        self.__session.close()


    def create_tables(self):
        Base.metadata.create_all(self.__engine)

    
    def drop_tables(self):
        Base.metadata.drop_all(self.__engine)

    
    def insert_data(self, data_list: list):
        self.__session.add_all(data_list)
        self.__session.commit()

    
    def get_shops_for_publisher(self, name_publisher: str)->list:
        
        q1 = self.__session.query(Book.title.label("book_title"), Book.id.label("book_id")).join(Publisher, Book.id_publisher==Publisher.id).filter(Publisher.name.like(f"%{name_publisher}%")).subquery()
        q2 = self.__session.query(q1.c.book_title, Stock.id_shop.label("shop_id"), Stock.id.label("stock_id")).join(q1, q1.c.book_id==Stock.id_book).subquery()
        q3 = self.__session.query(q2.c.book_title, q2.c.shop_id, Sale.date_sale, Sale.price).join(q2, q2.c.stock_id==Sale.id_stock).subquery()
        q4 = self.__session.query(q3.c.book_title, Shop.name, q3.c.price, q3.c.date_sale).join(q3, q3.c.shop_id==Shop.id).all()

        return q4
        