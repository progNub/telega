import json
from databases import database

file_name = "../databases/users.json"


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
    def read_from_json():
        data = []
        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                data = json.load(f)
                f.close()
                print("read complite")
        except IOError:
            print("file is non exists: " + file_name)
        return data
    @staticmethod
    def write_to_json(user):
        temp = User.read_from_json()
        temp.append(user.__dict__)
        try:
            with open(file_name, 'w+') as f:
                json.dump(temp, f, indent=2)
        except IOError:
            print("write is not complete: " + file_name)


    @staticmethod
    def write_to_DB(user):
        database.add_new_user(user)
    @staticmethod
    def get_users_from_DB(key="*"):
        return database.get_users_by_key(key)

    @staticmethod
    def check_unique(user):
        return database.check_enique(user.id)

