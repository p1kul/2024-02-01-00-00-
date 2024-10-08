import sqlite3

def initiate_db():
    connection = sqlite3.connect('gg.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE  TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    id = ['1', '2', '3', '4']
    title = ['Vitamins A', 'Vitamins B', 'Vitamins C', 'Vitamins D']
    description = ['Описание 1', 'Описание 2', 'Описание 3', 'Описание 4']
    price = ['100', '200', '300', '400']

    cursor.execute('INSERT INTO Products(id, title, description, price) VALUES (?, ?, ?, ?)',
                   (f'{id[0]}',f'{title[0]}', f'{description[0]}', f'{price[0]}'))
    cursor.execute('INSERT INTO Products(id, title, description, price) VALUES (?, ?, ?, ?)',
                   (f'{id[1]}',f'{title[1]}', f'{description[1]}', f'{price[1]}'))
    cursor.execute('INSERT INTO Products(id, title, description, price) VALUES (?, ?, ?, ?)',
                   (f'{id[2]}',f'{title[2]}', f'{description[2]}', f'{price[2]}'))
    cursor.execute('INSERT INTO Products(id, title, description, price) VALUES (?, ?, ?, ?)',
                   (f'{id[3]}',f'{title[3]}', f'{description[3]}', f'{price[3]}'))
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('gg.db')
    cursor = connection.cursor()
    all_info = cursor.execute('SELECT * FROM Products')
    all_info = cursor.fetchall()
    return list(all_info)



