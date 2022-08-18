# Example 1: Calculating product of all numbers from 1 to 10.

from re import X


product = 1
for n in range(1,10):
    product = product*n

print(product)    


## Video Exercise 1: 
# Factorial of a number is defined as the product of an integer and all the integers below it.
# For example, the factorial of four (4) is equal to 1*2*3*4=24.
# Write Factorial function that return the right no

def factorial(n):
    result = 1
    # remember the range function starts from zero. To accomodate 4, include the n+1 in the range.
    for i in range(1,n+1):
        result = result*i
    return result

print(factorial(4))
print(factorial(5))



## Example 3:


def to_celsius(x):
    return (x-32)*5/9

# the range function can receive 1, 2 or 3 parameters.
# If it receives 1 parameter it creates a sequence one by one until one less than the parameter received.
# If it receives 2 params, it will create a sequenc one by one from the 1st param until one less than the last param.
# If it receives 3 params, it will create a sequence until one than the second param; jumps will be the last param.

for x in range(0,101,10):
    print(x, to_celsius(x))
