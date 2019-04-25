# Write a Python script to concatenate following dictionaries to create
# a new one.

country = {'nepal': 'asia', 'congo': 'africa', 'estonia': 'europe'}
city = {'kathmandu': 'nepal', 'new delhi': 'india', 'beijing': 'china'}

places = {}
for place in (country, city):
    places.update(place)
print(places)
