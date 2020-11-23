import sqlite3

connection = sqlite3.connect('movies.db')

cursor = connection.cursor()

# cursor.execute("INSERT INTO Movies VALUES ('Taxi Driver', 'Martin Scorsese', 1976)")

# cursor.execute("SELECT * FROM Movies")

# famousFilms = [('Pulp Fiction', 'Quentin Tarantino', 1994),
# ('Back to the Future', 'Steven Spielberg', 1985),
# ('Moonrise Kingdom', 'Wes Anderson', 2012)]

# cursor.executemany('Insert INTO Movies VALUES (?,?,?)', famousFilms)

# records = cursor.execute("SELECT * FROM Movies")

# print(cursor.fetchall())

# for record in records:
# 	print(record)

# cursor.fetchone()

release_year = (1985,)

cursor.execute("SELECT * FROM Movies WHERE year=?", release_year)

print(cursor.fetchall())

connection.commit()

title = ('Pulp Fiction',)

cursor.execute("SELECT * FROM Movies WHERE title=?", title)
ct = 0
for i in cursor.fetchall():
    ct +=1
print(ct)
print(cursor.fetchall())

connection.commit()

connection.close()

