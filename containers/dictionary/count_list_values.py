# Write a Python program to count number of items in a dictionary value that
# is a list.

sample_dict = {
    "Alex": ["subj1", "subj2", "subj3"],
    "David": ["subj1", "subj2"],
    "Tom": "sub4",
}

count = 0
for value in sample_dict.values():
    if isinstance(value, list):
        count += 1

print(count)
