from databases import read_query, write_to_db


class Money(object):

    def __init__(self, sum=0, count=0, curs=0, BYN=0, RUB=0, USD=0, EUR=0):
        self.sum = sum
        self.count = count
        self.curs = curs
        self.BYN = BYN
        self.RUB = RUB
        self.USD = USD
        self.EUR = EUR



    @staticmethod
    def create_table_money():
        create_table_database = """CREATE TABLE money (
              idmoney INT PRIMARY KEY AUTO_INCREMENT PRIMARY KEY,
              user_id int not null,
              BYN FLOAT,
              RUB FLOAT,
              USD FLOAT,
              EUR FLOAT,
              CONSTRAINT money_id_users_id_fk 
                FOREIGN KEY (user_id) REFERENCES users (id));"""
        write_to_db(create_table_database)

    @staticmethod
    def add_money(user_id, money):
        sql = f"""INSERT INTO
        users ( 
        user_id, BYN, RUB, USD, EUR
        VALUES (
        '{user_id}', '{money.BYN}', '{money.USD}', '{money.RUB}', '{money.EUR}',
        );"""
        write_to_db(sql)
