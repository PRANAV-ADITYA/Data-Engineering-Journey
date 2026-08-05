import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger

logger = setup_logger('db_logger')
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
    cursor = connection.cursor(dictionary=True)
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
    logger.info(f"fetch_expenses_for_date called with {expense_date}")

# fetchall() retrieves those records from the mysql
    with get_db_cursor() as cursor:
        cursor.execute('select *  from expenses where expense_date = %s',(expense_date,))
        rows=cursor.fetchall()
        return rows

def insert_expense(expense_date, amount, category, notes):
    logger.info(f"Insert expense method calle with date:{expense_date} ")
    with get_db_cursor(commit = True) as cursor:
        cursor.execute(
    """
    INSERT INTO expenses
    (expense_date, amount, category, notes)
    VALUES (%s, %s, %s, %s)
    """,
    (expense_date, amount, category, notes)
)

def fetch_expenses_between_dates(start_date,end_date):
     logger.info(f"fetch_expense_between_dates called with start date:{start_date} and {end_date}")

     with get_db_cursor() as cursor:
            cursor.execute("select category,sum(amount) as total from expenses where expense_date between %s and %s group by category;",(start_date,end_date))
            data = cursor.fetchall()
     return data


def delete_expenses_for_date(expense_date):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))

def monthly_expenses():
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("select monthname(expense_date) as month,sum(amount) as total from expenses group by monthname(expense_date)")
        records  = cursor.fetchall()
        return records 


    


if __name__ == "__main__":
    print(fetch_expenses_between_dates("2024-08-01","2024-08-05"))
    
