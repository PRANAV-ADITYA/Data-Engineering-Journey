import mysql.connector


def get_db_cursor():
# Create a connection
    connection = mysql.connector.connect(
        host = 'localhost',
    user = 'root',
    password = '5096193Pr$',
    database= 'expense_manager'
    )

# Check if the connection is successful or not 
    if (connection.is_connected()):
        print("Connection Successful")
    else:
        print("Failed in connecting to a database")

# Create a cursor to execute the sql queries
    cursor = connection.cursor()
    return connection,cursor


def fetch_all_records():
    connection,cursor = get_db_cursor()
    cursor.execute('select * from expenses')
# fetchall() retrieves those records from the mysql
    rows=cursor.fetchall()
    for row in rows:
        print(row)
    connection.close()




def fetch_records_for_date(expense_date):
    connection,cursor = get_db_cursor()
    cursor.execute('select * from expenses where expense_date = %s',(expense_date,))

# fetchall() retrieves those records from the mysql
    rows=cursor.fetchall()
    for row in rows:
        print(row)
    connection.close()

fetch_records_for_date("2024-08-01")