import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


# dialect+driver://username:password@host:port/database

# Устанавливаем соединение с postgres
connection = psycopg2.connect(user="postgres", password="postgres")
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Создаем курсор для выполнения операций с базой данных
cursor = connection.cursor()

# Создаем базу данных
sql_create_database = cursor.execute('create database users')

# Закрываем соединение
cursor.close()
connection.close()