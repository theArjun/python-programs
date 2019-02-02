# This function resembles with the range function; done using generator function

def range_function(numOne, numTwo):
    while numOne < numTwo:
        yield numOne
        numOne += 1
        
result = range_function(30,40)

for i in result:
    print(i)