import sqlite3

connect = sqlite3.connect('db/baza/list.db')
cursor = connect.cursor()

#Створити базу даних
def db_plus():
    cursor.execute(""" CREATE TABLE IF NOT EXISTS expenses(name TEXT, last_name TEXT, id INT) """)
    connect.commit()

#Видалити базу даних
def db_delete():
    cursor.execute("DROP TABLE expenses")
    connect.commit()

#Занести дані у базу даних
def add_data_db(name_register, ba, c):
    main_list = [name_register, ba, c]
    cursor.execute("INSERT INTO expenses VALUES(?,?,?);", main_list)
    connect.commit()

