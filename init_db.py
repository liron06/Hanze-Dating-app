import sqlite3

connection = sqlite3.connect('datingsite.db')
cursor = connection .cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS gebruikers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    gebruikersnaam TEXT UNIQUE NOT NULL,
    wachtwoord TEXT NOT NULL
    )
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS profielen (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    gebruiker_id INTEGER UNIQUE NOT NULL,
    naam TEXT NOT NULL,
    foto_url TEXT NOT NULL,
    leeftijd INTEGER NOT NULL,
    geslacht TEXT NOT NULL,
    bio TEXT NOT NULL,
    FOREIGN KEY (gebruiker_id) REFERENCES gebruikers (id)
    )
''')

connection.commit()
connection.close()

print('Database is aangemaakt!')