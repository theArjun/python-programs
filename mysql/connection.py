import mysql.connector

my_db = mysql.connector.connect(host="localhost", user="root", passwd="")

# MYSQLConnection object
print(my_db)

my_cursor = my_db.cursor()
print(my_cursor)

# Prints list of databases in system.
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)

# Creates a database
# This is non-select query, so returns None.
result = my_cursor.execute("CREATE DATABASE IF NOT EXISTS `arjun` ")
print(result)

# Creates a table
# Insert a back slash / space to write a long string with PEP-8 Standard
result = my_cursor.execute(
    "CREATE TABLE IF NOT EXISTS `arjun`.`college`("
    "id INT PRIMARY KEY AUTO_INCREMENT,"
    "rank VARCHAR(32) NOT NULL,"
    "college_name VARCHAR(200) NOT NULL)"
)
print(result)

# Displays list of tables
my_cursor.execute("USE `arjun`")
result = my_cursor.execute("SHOW TABLES")
print(result)

# Insert data into table
try:
    sql_query = "INSERT INTO `arjun`.`college` VALUES ('Third', 'GCES')"
    my_cursor.execute(sql_query)
except (mysql.connector.errors.InternalError) as e:
    print(e)
    print("Error while inserting.")
    print("Maybe, the data is already inserted.")
else:
    print("Successfully inserted.")
