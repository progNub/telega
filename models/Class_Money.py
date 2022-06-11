from databases import read_query, write_to_db


class Money(object):
    def __init__(self, BYN=0, RUB=0, USD=0, EUR=0):
        self.curs = Money._get_curs(BYN, RUB, USD, EUR)
        self.BYN = BYN
        self.RUB = RUB
        self.USD = USD
        self.EUR = EUR

    @staticmethod
    def get_usd(user_id):
        sql = f"""SELECT byn, usd, curs FROM money WHERE user_id = {user_id} AND usd > 0"""
        return read_query(sql)

    @staticmethod
    def get_rub(user_id):
        sql = f"""SELECT byn, rub, curs FROM money WHERE user_id = {user_id} AND rub > 0"""
        return read_query(sql)

    @staticmethod
    def get_eur(user_id):
        sql = f"""SELECT byn, eur, curs FROM money WHERE user_id = {user_id} AND eur > 0"""
        return read_query(sql)

    @staticmethod
    def get_list_writes_str(user_id):
        usd = Money.get_usd(user_id)
        rub = Money.get_rub(user_id)
        eur = Money.get_eur(user_id)
        str_usd = "BYN - USD\n"
        str_eur = "BYN - EUR\n"
        str_rub = "BYN - RUB\n"
        count1 = 0
        count2 = 0
        count3 = 0
        for i in usd:
            count1 += 1
            str_usd += "{}. {:^10.3f} : {:^10.3f}\n".format(count1, i[0], i[1])
        str_usd += "\n"
        for i in eur:
            count2 += 1
            str_eur += "{}. {:^10.3f} : {:^10.3f}\n".format(count2, i[0], i[1])
        str_eur += "\n"
        for i in rub:
            count3 += 1
            str_rub += "{}. {:^10.3f} : {:^10.3f}\n".format(count3, i[0], i[1])
        str_rub += "\n"

        return str_usd + str_eur + str_rub

    @staticmethod
    def get_sum_money_str(user_id):
        temp_list = Money.get_monet_from_db(user_id)
        byn = usd = eur = rub = 0
        for i in temp_list:
            byn += i[3]
            rub += i[4]
            usd += i[5]
            eur += i[6]
        string_byn = f"Общая сумма потраченых: BYN = '{byn}'\n"
        string_eur = f"Общая сумма купленных:  EUR = '{eur}'\n"
        string_usd = f"Общая сумма купленных:  USD = '{usd}'\n"
        string_rub = f"Общая сумма купленных:  RUB = '{rub}'\n"
        return string_byn + string_eur + string_usd + string_rub

    @staticmethod
    def _get_curs(BYN=0, RUB=0, USD=0, EUR=0):
        result = 0
        if (BYN != 0 and RUB != 0) \
                or (BYN != 0 and USD != 0) \
                or (BYN != 0 and EUR != 0):
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
        self.curs = Money._get_curs(BYN, RUB, USD, EUR)
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
        {user_id},{money.curs},{money.BYN}, {money.RUB}, {money.USD}, {money.EUR});"""
        write_to_db(sql)

    @staticmethod
    def get_monet_from_db(user_id):
        sql = f"""select * from money WHERE user_id = {user_id};"""
        return read_query(sql)

    @staticmethod
    def checking_null(id_user):
        sql = f"""select * from money where user_id = '{id_user}'"""
        return bool(len(read_query(sql)))

Money.drop_table_money()
Money.create_table_money()