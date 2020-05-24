import json
import mysql.connector


json_database = mysql.connector.connect(
    host="localhost", user="root", passwd="", database="arjun"
)

# Create a cursor for the database.
json_cursor = json_database.cursor()

# Create table.
json_cursor.execute(
    "CREATE TABLE IF NOT EXISTS `json_data`("
    "id INT PRIMARY KEY AUTO_INCREMENT,"
    "first_name VARCHAR(32),"
    "last_name VARCHAR(32),"
    "email VARCHAR(32),"
    "gender VARCHAR(32),"
    "phone_number VARCHAR(32)"
    ")"
)

# Open JSON file in read mode.
json_file = open("MOCK_DATA.json", "r")

# Read file and load the JSON string.
json_data = json.loads(json_file.read())

for data_count in range(1, 100):
    # Read the respective values from Python Dictionary.
    first_name = json_data[data_count]["first_name"]
    last_name = json_data[data_count]["last_name"]
    email = json_data[data_count]["email"]
    gender = json_data[data_count]["gender"]
    phone_number = json_data[data_count]["phone_number"]

    # Insertion query
    sql = "INSERT INTO `arjun`.`json_data`(`first_name`, `last_name`, `email`, `gender`, `phone_number`) VALUES ('{}', '{}', '{}', '{}', '{}')".format(
        first_name, last_name, email, gender, phone_number
    )

    # Executes insertion query and commiting(writing) files to database.
    json_cursor.execute(sql)
    json_database.commit()

# Closing JSON file which was opened in read mode.
json_file.close()
