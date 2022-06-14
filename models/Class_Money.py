from databases import read_query, write_to_db


class Money(object):
    def __init__(self, BYN=0, RUB=0, USD=0, EUR=0):
        self.curs = Money._get_curs(BYN, RUB, USD, EUR)
        self.BYN = BYN
        self.RUB = RUB
        self.USD = USD
        self.EUR = EUR

    @staticmethod
    def get_curr_and_curs(user_id, usd=False, eur=False, rub=False):
        sql = ""
        if usd:
            sql = f"""SELECT byn, usd, curs FROM money WHERE user_id = {user_id} AND usd > 0"""
        elif rub:
            sql = f"""SELECT byn, rub, curs FROM money WHERE user_id = {user_id} AND rub > 0"""
        elif eur:
            sql = f"""SELECT byn, eur, curs FROM money WHERE user_id = {user_id} AND eur > 0"""
        return read_query(sql)

    @staticmethod
    def get_list_writes_str(user_id):
        result_str = ''
        usd = Money.get_curr_and_curs(user_id, usd=True)
        rub = Money.get_curr_and_curs(user_id, rub=True)
        eur = Money.get_curr_and_curs(user_id, eur=True)
        str_usd = "{:>6}  {:>9} {:>11}\n".format("BYN", "USD", "Курс")
        str_eur = "{:>6}  {:>9} {:>11}\n".format("BYN", "EUR", "Курс")
        str_rub = "{:>6}  {:>9} {:>11}\n".format("BYN", "RUB", "Курс")
        count_usd = count_eur = count_rub = 0
        for i in usd:
            count_usd += 1
            str_usd += "{}. {:<8}{:^3}{:<8} : {:>}\n".format(count_usd, i[0], '=', i[1], i[2])
        str_usd += "\n"
        for i in eur:
            count_eur += 1
            str_eur += "{}. {:<8}{:^3}{:<8} : {:>}\n".format(count_eur, i[0], '=', i[1], i[2])
        str_eur += "\n"
        for i in rub:
            count_rub += 1
            str_rub += "{}. {:<8}{:^3}{:<8} : {:>}\n".format(count_rub, i[0], '=', i[1], i[2])
        str_rub += "\n"
        if count_usd != 0:
            result_str += str_usd
        if count_eur != 0:
            result_str += str_eur
        if count_rub != 0:
            result_str += str_rub
        return result_str

    @staticmethod
    def get_sum_money_str(user_id):
        temp_list = Money.get_monet_from_db(user_id)
        byn = usd = eur = rub = 0
        for i in temp_list:
            byn += i[3]
            rub += i[4]
            usd += i[5]
            eur += i[6]
        result_str = string_byn = "Затрачено: BYN = {:>.2f}\n\n".format(byn)
        string_eur = "Куплено: EUR = {:>.2f}\n".format(eur)
        string_usd = "Куплено: USD = {:>.2f}\n".format(usd)
        string_rub = "Куплено: RUB = {:>.2f}\n".format(rub)
        if not rub == 0:
            result_str += string_rub
        if not eur == 0:
            result_str += string_eur
        if not usd == 0:
            result_str += string_usd
        return result_str

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
        sql_del = "drop table money;"
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
        sql = f"select * from money WHERE user_id = {user_id};"
        return read_query(sql)

    @staticmethod
    def checking_null(id_user):
        sql = f"select * from money where user_id = '{id_user}'"
        return bool(len(read_query(sql)))

    @staticmethod
    def delete_all_writes_about_money(id_user):
        sql = f"delete from money where user_id = {id_user};"
        result = write_to_db(sql)
        if not result:
            print(f"не получилось удалить записи пользователя под id = {id_user}")
        return result
