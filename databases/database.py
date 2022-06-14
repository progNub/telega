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


def write_to_db(query, connection=create_connection()):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        return True
    except Error as e:
        print(f"error '{e}'")
        return False


def read_query(query, connection=create_connection()):
    connection.reconnect()
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Error '{e}'")
    return result
