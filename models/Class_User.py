import json
import os.path

from databases import read_query, write_to_db, create_connection


file_name_users = "E:/Python_2022/telega/databases/users.json"


class User(object):
    def __init__(self, user):
        self.id = user.id
        self.is_bot = user.is_bot
        self.first_name = user.first_name
        self.last_name = user.last_name
        self.username = user.username
        self.language_code = user.language_code
        self.can_join_groups = user.can_join_groups
        self.can_read_all_group_messages = user.can_read_all_group_messages
        self.supports_inline_queries = user.supports_inline_queries

    @staticmethod
    def add_new_user(user):
        write_user = f"""INSERT INTO
            users ( id_telegram,
            is_bot,
            first_name,
            last_name,
            username,
            language_code,
            can_join_groups,
            can_read_all_group_messages,
            supports_inline_queries)
            VALUES (
            {user.id},
            {user.is_bot},
            '{user.first_name}',
            '{user.last_name}',
            '{user.username}',
            '{user.language_code}',
            '{user.can_join_groups}',
            '{user.can_read_all_group_messages}',
            '{user.supports_inline_queries}');"""
        write_to_db(write_user)

    @staticmethod
    def check_unique(user_id):
        check = f"(select * from users where id_telegram = '{user_id}');"
        return bool(len(read_query(check)))

    @staticmethod
    def delete_user(id_user):
        delete_user = f"""DELETE FROM users WHERE id_telegram = '{id_user}'; """
        write_to_db(delete_user)

    @staticmethod
    def create_database_table_users():
        create_table_database = """CREATE TABLE users
            (
                id INT AUTO_INCREMENT primary key not null,
                id_telegram int not null UNIQUE,
                is_bot bool,
                first_name char(255),
                last_name char(255),
                username char(255),
                language_code char(255),
                can_join_groups char(255),
                can_read_all_group_messages char(255),
                supports_inline_queries char(255));"""
        write_to_db(create_table_database)

    @staticmethod
    def get_users_by_key(key='*'):
        return read_query(f"select {key} from users;")

    @staticmethod
    def write_to_DB(user):
        User.add_new_user(user)

    @staticmethod
    def get_users_from_DB(key="*"):
        return User.get_users_by_key(key)

# @staticmethod
# def read_from_json():
#     data = []
#     if os.path.exists(file_name_users):
#         data = []
#         try:
#             with open(file_name_users, 'r') as f:
#                 data = json.load(f)
#                 f.close()
#                 print("read complite")
#         except IOError:
#             print("file is non exists: " + file_name_users)
#     else:
#         print(file_name_users + " not exists, but created")
#     return data
#
# @staticmethod
# def write_to_json(user):
#     temp = User.read_from_json()
#     temp.append(user.__dict__)
#     try:
#         with open(file_name_users, 'w+') as f:
#             json.dump(temp, f, indent=2)
#     except IOError:
#         print("write is not complete: " + file_name_users)
