# bot info
TOKEN = "5579850884:AAHfWR8fOm5KPeo-DfSZWTyse9aRaXc728g"

# databases info
HOST_NAME = "localhost"
USER_NAME = "root"
USER_PASSWORD = "root"
DB_NAME = "telebot"

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
    supports_inline_queries char(255)
);"""
