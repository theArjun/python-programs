print("Set Type\n\nA set sequence doesnt allow to make duplicates of element(unique) and elements are immutable. (which cant be changed).")

print("But the set itself is mutable. We can add or remove items fro it.")

print("Sets are used to perform mathematical operations like unions, intersection, symmetric difference etc.")

s= {} 

print(type(s)) # It returns type dictionary.

s= {1,2,3,4,"Arjun",1}
print(len(s)) # Last element 1 is discarded and the length is returned 5.
print(type(s))


