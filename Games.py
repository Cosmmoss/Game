import sqlite3
class Games:
    def __init__(self, name, zhanr, year, age_limit, price):
        self.name = name
        self.zhanr = zhanr
        self.year = year
        self.age_limit = age_limit
        self.price = price
        conn = sqlite3.connect('Games.db')
        cursor = conn.cursor()
        sql_insert = 'INSERT INTO Games(name, zhanr, year, age_limit, price) VALUES(?, ?, ?, ?, ?)'
        data = (self.name, self.zhanr, self.year, self.age_limit, self.price)
        cursor.execute(sql_insert, data)
        conn.commit()
        conn.close()
    def __str__(self):
        return f'Название игры: {self.name}, Жанр игры: {self.zhanr}, Год выпуска игры: {self.year},\
 Возрастной лимит: {self.age_limit}, Цена игры: {self.price}'
    
num_add_game = int(input('Укажите количество игр для добавления: '))
for i in range(num_add_game):
    game = Games(input('Название игры: '), input('Жанр игры: '), \
             input('Год выпуска игры: '), input('Возрастной лимит игры: '),\
             input('Цена игры: '))
    print(game)

import sqlite3
con = sqlite3.connect('games.db')  # Подключитесь к базе данных
                                   
cur = con.cursor()
cur.execute('SELECT * FROM Games')
res = cur.fetchall()
con.close()
for row in res:  # выведите в консоль список игр
    print('Игра №', row[4], ':', row)
num_game = int(input('Выберите, понравившуюся игру \
и укажите её номер для скачивания: '))  # предложив пользователю скачать одну 
                                               # из игр. Запросите у пользователя игру, 
                                               # которую он желает скачать из представленных
'''После ответа пользователя, происходит “скачивание” игры, если таковая имеется 
в списке – нужно обновить (UPDATE) информацию в базе данных. Необходимо увеличить 
значение столбца, в котором хранится кол-во скачиваний по выбранной игре, на единицу'''
con = sqlite3.connect('games.db')
cur = con.cursor()
cur.execute(f"UPDATE Games SET number_of_downloads = \
        number_of_downloads + 1 WHERE ROWID = {num_game}")
con.commit()  # чтобы сохранить изменения
con.close()
print(res[num_game - 1])  # вывод игры, которую выбрали для скачивания

    