import sqlite3

connection = sqlite3.connect('database.db')
print('Opened database successfully')

connection.execute('CREATE TABLE movies (name TEXT, year INTEGER, rating REAL, genre TEXT, plot TEXT)')
print('Movie Table created successfully')

connection.close()
