import sqlite3

# connection() makes connection to the database using the database file as an input argument
def connection(db_name):
    try:
        # creates a connection object to an SQLite database using the sqlite3.connect()
        conn = sqlite3.connect(db_name)
        # displays a message indicating that the database was opened successfully if the connection is successful,
        print("opened database successfully")
        # returns the connection object
        return conn
    except Exception as e:
        # displays an error message that contains the exception message if an exception is thrown during the connection attempt.
        print("Error during making the connection: ", str(e))

# calls the 'connection' function with the parameter 'mydatabase.db' to create a connection object to an SQLite database
conn = connection('mydatabase.db')

# creates a cursor object from the connection object to execute SQL commands
curs = conn.cursor()