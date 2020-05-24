import json


my_dictionary = {
    "id": 1,
    "first_name": "Wake",
    "last_name": "Frayne",
    "email": "wfrayne0@nih.gov",
    "gender": "Male",
    "phone_number": "323-989-5058",
}

# dumps() method converts Python dictionary to json string.
# indent indents json string according to passed numeric value.
# sort_keys helps sort the keys alphabetically.
created_json = json.dumps(my_dictionary, indent=4, sort_keys=True)
print(created_json)
print(type(created_json))
