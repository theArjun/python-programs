# Lambdas

A lambda function is a small anonymous function that doesn't have any name. It can take any number of arguments, but can only have one expression.

## Syntax
        lambda arguments : expression 

## Example

A lambda function that adds 10 to the number passed in as an argument, and print the result:  

        x = lambda a : a + 10
        print(x(5)) 

It is widely used inside other functions : ```filter, map, reduce```.