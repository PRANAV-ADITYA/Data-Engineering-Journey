import mysql.connector
from contextlib import contextmanager


@contextmanager
def get_db_cursor(commit = False):
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
    yield cursor

    if(commit):
        connection.commit()


    cursor.close()
    connection.close()

def fetch_all_records():
    
# fetchall() retrieves those records from the mysql
    with get_db_cursor() as cursor:
        cursor.execute('select * from expenses')
        rows=cursor.fetchall()
        for row in rows:
            print(row)


def fetch_records_for_date(expense_date):

# fetchall() retrieves those records from the mysql
    with get_db_cursor() as cursor:
        cursor.execute('select * from expenses where expense_date = %s',(expense_date,))
        rows=cursor.fetchall()
        for row in rows:
            print(row)

def insert_expense(id, expense_date, amount, category, notes):
    with get_db_cursor(commit = True) as cursor:
        cursor.execute(
            "INSERT INTO expenses  VALUES (%s,%s, %s, %s, %s)",
            (id, expense_date, amount, category, notes)
        )

# fetch_records_for_date("2024-08-01")

insert_expense(10,"2024-08-20", 300, "Food", "Panipuri")

