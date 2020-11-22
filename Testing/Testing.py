'''
Created on Nov 22, 2020

@author: AndyY
'''

import sqlite3

connection = sqlite3.connect('horses-sqlite.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Horses 
(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, 
    breed TEXT, height REAL, birthday TEXT)''')

usersToInsert = [('Babe', 'Quarter Horse',15.3,'2015-02-10')]

cursor.executemany('''INSERT INTO Horses(name, breed, height, birthday) 
    VALUES (?,?,?,?)''', usersToInsert)

cursor.execute("SELECT name FROM Horses")
print(cursor.fetchall())

cursor.execute("SELECT * FROM Horses")
print(cursor.fetchall())

connection.commit()
connection.close()
