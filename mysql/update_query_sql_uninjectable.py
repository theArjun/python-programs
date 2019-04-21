import mysql.connector


my_database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="arjun"
)

my_cursor = my_database.cursor()
# Using wildcards help to prevent SQL Injection.
sql_query = "UPDATE college SET rank = %s WHERE id = 1"
# Tuple - values
values = ('Tenth',)

my_cursor.execute(sql_query, values)
my_database.commit()

print('{} rows afftected.'.format(my_cursor.rowcount))
