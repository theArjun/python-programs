import mysql.connector


my_database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="arjun"
)

sql_query = "UPDATE college SET rank = 'First' WHERE id = 1"
my_cursor = my_database.cursor()
my_cursor.execute(sql_query)
# Notice the statement: mydb.commit(). It is required to make the changes,
# otherwise no changes are made to the table.
my_database.commit()
print('{} rows affected.'.format(my_cursor.rowcount))
