import sqlite3
from sqlite3 import Error

# NOTE: Do not modify
# Creates a sqlite3 database connection (in memory)
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(":memory:")
        return conn
    except Error as e:
        print(e)
    
    return conn

# Creates a table
def create_table(conn, create_table_sql):
    # FIXME: Type your code here
    cursor = conn.cursor()
    cursor.execute(create_table_sql)
    
# Inserts horse data as a row in the database
def insert_horse(conn, data):
    cursor = conn.cursor()
    cursor.executemany('''INSERT INTO Horses(name, breed, height, birthday) 
    VALUES (?,?,?,?)''', data)
    # FIXME: Type your code here

# Prints all rows of data fromthe horses table
def select_all_horses(conn):
   # FIXME: Type your code here
   cursor = conn.cursor()
   cursor.execute("SELECT * FROM Horses")
   print ('All Horses:')
   for x in cursor.fetchall():
       print (x)
   #print(cursor.fetchall())

if __name__ == '__main__':
    database = r"HorseStable.db"

    # FIXME 1: Call the create_connection function to connect to the database HorseStable.db
    conn = create_connection(database)
    
    # FIXME 2: Create the sql statement string to create a table
    table_str= "CREATE TABLE IF NOT EXISTS Horses (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, breed TEXT, height REAL, birthday TEXT)"

    # FIXME 3: Call the create_table function passing the sql statement string
    create_table(conn, table_str)
    
    # FIXME 4: Insert the horse data into the database
    horseToInsert = [('Babe', 'Quarter Horse',15.3,'2015-02-10')]
    insert_horse(conn, horseToInsert)
    
    # FIXME 5: Print out all hourses by calling the select_all_horses function
    select_all_horses(conn)
