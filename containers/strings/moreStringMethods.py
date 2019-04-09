s= "Nepal is Awesome."

# Find Method
print(s.find("we")) # This returns the initial index of the letter 'w'

print(s.find("we"),0,16) # The first parameter is the string to be searched, second one is the initial starting index of the string whereas the last parameter specifies the last index of the string till which the desired string is to be searched.

# Count Method
print(s.count("a")) # Cound how much it occured/appered in string

# Replace Method
print(s.replace("we", "our")) # Replaces the old string by the new one.

#Converts to Uppercase
print(s.upper())

#Converts to Lowercase
print(s.lower())

#Converts to Title Case which means the initial letter of every word is capitalized.
print(s.title())
