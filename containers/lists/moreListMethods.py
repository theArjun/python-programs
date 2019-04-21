lst = [10, 20, "Arjun", 50.67]

# lst.clear() I still wonder, why I got the error message here.
print(lst)

print(max(lst))  # Prints the maximum value in the list
print(min(lst))  # Prints the minimum value in the list

lst.insert(3, 99)  # Inserts the value 99 at index 3
print(lst)
lst.insert(2, "Adhikari")  # Inserts the value Adhikari at index 2
print(lst)

lst.sort()  # Sorts the array in ascending order
print(lst)

lst.sort(reverse=True)  # Sorts the list in descending order
print(lst)
