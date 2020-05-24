#  Write a Python script to check if a given key already exists in a dictionary

sample_dict = {"nepal": "asia", "congo": "africa", "estonia": "europe"}

sample_country = input()

if sample_country in sample_dict:
    print("Already in Dictionary")
else:
    print("Not in Dictionary")
