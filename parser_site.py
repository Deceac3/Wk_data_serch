def analys_check():
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT id FROM profile BY id')
    results = cursor.fetchall()
