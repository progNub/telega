import json

file_name = "users.json"


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

    def check_unique(self, user):
        data = user.read_from_json()
        result = True
        if len(data):
            for i in data:
                if i["id"] == user.id:
                    result = False
        return result

    def read_from_json(self):
        data = []
        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                data = json.load(f)
                f.close()
                print("read complite")
        except IOError:
            print("file is non exists: " + file_name)
        return data

    def write_to_json(self, user):
        temp = User.read_from_json(self)
        temp.append(user.__dict__)
        try:
            with open(file_name, 'w+') as f:
                json.dump(temp, f, indent = 2)
                print("write complite")
        except IOError:
            print("write is not complete: " + file_name)
