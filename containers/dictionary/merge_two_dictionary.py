# Write a Python script to merge two Python dictionaries.

country = {'nepal': 'asia', 'congo': 'africa', 'estonia': 'europe'}
city = {'kathmandu': 'nepal', 'new delhi': 'india', 'beijing': 'china'}

print(country)

# Merging two dictionary.
for city_ in city:
    country.update(city)

print(country)
