import mysql.connector


try:
    my_db = mysql.connector.connect(host="localhost", user="root", passwd="")
except ConnectionRefusedError:
    print("Error in MYSQL Connection.")

sql_query = "SELECT * FROM `arjun`.`college`"
my_cursor = my_db.cursor()
my_cursor.execute(sql_query)

# We use the fetchall() method, which fetches all rows from the last executed
# statement.
for data in my_cursor.fetchall():
    print(data)

# If we're interested in one row, we can use fetchone().
print(my_cursor.fetchone())
