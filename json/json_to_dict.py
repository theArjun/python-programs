import json


# JSON should be sorrounded by single quote, as it's a string.
json_data = '{"id": 1, "first_name": "Wake", "last_name": "Frayne", "email": "wfrayne0@nih.gov", "gender": "Male", "phone_number": "323-989-5058"}'
print(type(json_data))

# It's a dictionary after loading.
loaded_json = json.loads(json_data)
print(type(loaded_json))

print(loaded_json["last_name"])
