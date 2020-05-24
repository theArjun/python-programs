import json


# Step 1 : Read the file
# Step 2 : Load the JSON string
# Step 3 : Open another file in write mode
# Step 4 : Dump the loaded JSON string
# Step 5 : Write and close the open files.

my_json = open("MOCK_DATA.json", "r")
# Returns string data type
print(type(my_json.read()))

my_json.seek(0)
created_json_string = my_json.read()
created_json_string = json.loads(created_json_string)
# print(created_json_string)

file_json = open("INDENTED_DATA.json", "w")
file_json_data = json.dumps(created_json_string, indent=4, sort_keys=True)
print(file_json_data)
file_json.write(file_json_data)

my_json.close()
file_json.close()

# To check whether file is properly intended or not.
sample = open("INDENTED_DATA.json", "r")
my_data = sample.read()
print(my_data)
