import mysql
from mysql.connector import Error

from config import HOST_NAME, USER_NAME, USER_PASSWORD, DB_NAME


def create_connection(host_name=HOST_NAME, user_name=USER_NAME, user_password=USER_PASSWORD, db_name=DB_NAME):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name)
    except Error as e:
        print(f"error '{e}' ")
    return connection


def write_to_db(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("select completed")
        connection.commit()
    except Error as e:
        print(f"error '{e}'")


def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Error '{e}'")
    return result


def delete_user(id_user):
    delete_user = f"""DELETE FROM users WHERE id_telegram = '{id_user}' """
    write_to_db(create_connection(), delete_user)


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
    write_to_db(create_connection(), write_user)


def check_enique(user_id):
    query = f"(select * from users where id_telegram = {user_id});"
    return bool(len(read_query(create_connection(), query)))


def get_users_by_key(key='*'):
    return read_query(create_connection(), f"select {key} from users;")


def create_base_data_users():
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
    write_to_db(create_connection(), create_table_database)


