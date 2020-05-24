# Write a Python program to remove spaces from dictionary keys.

sample_dict = {"arkjas fnaksjdlf ": 3, "s  sadvfa": 3, "   d sadfasd": 3}

for key in sample_dict.keys():
    print(key.strip().replace(" ", ""))
