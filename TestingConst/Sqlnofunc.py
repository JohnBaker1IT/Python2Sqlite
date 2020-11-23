import csv, sqlite3
from sqlite3 import Error

# TODO: Implement this function
# inserts new writer data as a row in the database. Insert both name and number of works.
def insert_writer(con, data):
    return 0

# TODO: Implement this function
# updates an existing writer record based on writer name
def update_writer(con, writer):
    return 0

# TODO: Implement this function
# Check if the writer's name exists in the database
# Return the number of records found (should be 1 if writer exits, or 0 if the writer doesn't exist in table)
def check_writer(con, name):
    return 0

# NOTE: Do not modify
# Creates a sqlite3 database connection (in memory)
def create_connection():
    """ create a database connection to a SQLite database """
    con = None
    try:
        con = sqlite3.connect(":memory:")
        return con
    except Error as e:
        print(e)

    return con

# NOTE: Do not modify
# Creates a table
def create_table(con, create_table_sql):
    """ create a table from the create_table_sql statement
    :param cnn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = con.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

# NOTE: Do not modify
# Prints all rows of data from the writers table
def select_all_writers(con):
    """
    Query all rows in the tasks table
    :param con: the Connection object
    :return:
    """
    cursor = con.cursor()
    cursor.execute("SELECT * FROM writers")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

# NOTE: Do not modify
# Initializes the database by adding all rows from the allWorks.csv file
def initialize_database(con):

    cursor = con.cursor()

    ## create writers table
    create_table_sql = """ CREATE TABLE writers (
                                id integer PRIMARY KEY NOT NULL,
                                name text,
                                num integer
                            ); """
    create_table(con, create_table_sql)

    ## Read contents of CSV file
    filename = 'allWorks.csv'
    with open(filename, 'r') as fin:  
        dr = csv.DictReader(fin)  # comma is default delimiter
        to_db = [(i['Name'], i['Number of works']) for i in dr]

    ## Insert contents of CSV file into writers table
    #print(to_db)
    cursor.executemany("INSERT INTO writers (name, num) VALUES (?, ?);", to_db)
    con.commit()

if __name__ == '__main__':

    # TODO: Create a database connection
    con = create_connection()
    
    # Initialize database data
    initialize_database(con)

    
    print('Would you like to update a writer database record?')
    yesNo = input()
    if yesNo[0] == 'y' or yesNo[0] == 'Y':

        # Loop until user is done updating records
        while yesNo == 'y' or yesNo == 'Y':
            print('Which entry would you like to update?')
            name = input()
            #name = 'J.K. Rowling'
            

            # TODO Check if writer exists in database    ###nec
            cursor = con.cursor()
            
            cursor.execute("SELECT * FROM writers WHERE Name=?", (name,))
            ct = 0
            for i in cursor.fetchall():
                print (i)
                ct +=1
            print('ct',ct)
            
            con.commit()
            
            
            
            if (ct>0 ):
                print('Enter a new value for ' + name)
                num = input()
                # TODO Update writer's value for number of works
                sql_update_query = 'Update writers set Num = '+num+' where Name = ?'
                #print(sql_update_query)
                cursor.execute(sql_update_query,(name,))
                con.commit()
                
                cursor.execute("SELECT * FROM writers")
                print(cursor.fetchall())
                con.commit()
        
            else:
                print("Entry not found. Add new entry?")
                yesNo = input()
                if yesNo[0] == 'y' or yesNo[0] == 'Y':
                    print('Number of works?')
                    num = input()
                    usersToInsert = [(name, num)]
                    cursor.executemany('''INSERT INTO writers(Name, Num) 
                    VALUES (?,?)''', usersToInsert)
                    # TODO Insert new writer entry
                    cursor.execute("SELECT * FROM writers")
                    print(cursor.fetchall())
                    con.commit()
                    
            print('Would you like to continue to update writers')
            yesNo = input()

    print("(ID, Name, Num)")
    select_all_writers(con)
    con.close()