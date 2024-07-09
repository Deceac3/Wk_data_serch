import sqlite3
def data_base_up():
    up_dataBase = sqlite3.connect('Vk_profiles_database.db')
    cursor = up_dataBase.cursor()

    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS profile(
        id TEXT NOT NULL,
        full_name TEXT NOT NULL,
        location TEXT NOT NULL,
        description TEXT NOT NULL,
        friends_count NEXT NOT NULL,
        birthday TEXT NOT NULL,
        relateship TEXT NOT NULL
        )'''
    )

    up_dataBase.commit()
    up_dataBase.close()

    