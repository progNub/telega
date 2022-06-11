from databases import read_query, write_to_db


class Money(object):

    def __init__(self, BYN=0, RUB=0, USD=0, EUR=0):
        self.curs = Money.get_curs(BYN, RUB, USD, EUR)
        self.BYN = BYN
        self.RUB = RUB
        self.USD = USD
        self.EUR = EUR

    @staticmethod
    def get_curs(BYN=0, RUB=0, USD=0, EUR=0):
        result = 0
        if (BYN != 0 and RUB != 0) \
                or (BYN != 0 and USD != 0) \
                or (BYN != 0 and EUR != 0):
            curs = 0
            if RUB != 0:
                curs = BYN / RUB
                result = float('{:.5f}'.format(curs))
            elif EUR != 0:
                curs = BYN / EUR
                result = float('{:.5f}'.format(curs))
            elif USD != 0:
                curs = BYN / USD
                result = float('{:.5f}'.format(curs))
        return result

    def set_money(self, BYN=0, RUB=0, USD=0, EUR=0):
        self.curs = Money.get_curs(BYN, RUB, USD, EUR)
        self.BYN = BYN
        self.RUB = RUB
        self.USD = USD
        self.EUR = EUR

    @staticmethod
    def create_table_money():
        create_table_database = """CREATE TABLE money (
  id INT PRIMARY KEY AUTO_INCREMENT PRIMARY KEY,
  user_id int not null,
  curs FLOAT,
  byn FLOAT,
  rub FLOAT,
  usd FLOAT,
  eur FLOAT,
  CONSTRAINT money_id_users_id_fk 
    FOREIGN KEY (user_id) REFERENCES users (id_telegram)
    ON DELETE CASCADE);"""
        write_to_db(create_table_database)

    @staticmethod
    def drop_table_money():
        sql_del = """drop table money;"""
        write_to_db(sql_del)

    @staticmethod
    def add_money(user_id, money):
        sql = f"""INSERT INTO
        money ( 
        user_id, curs, byn, rub, usd, eur)
        VALUES (
        {user_id},{money.curs},{money.BYN}, {money.USD}, {money.RUB}, {money.EUR});"""
        write_to_db(sql)

    @staticmethod
    def get_monet_from_db(user_id):
        sql = f"""select * from money WHERE user_id = {user_id};"""
        return read_query(sql)



