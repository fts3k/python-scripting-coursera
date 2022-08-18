# Recursion - repeated application of the same procedure to a smaller problem.
# Is a way of doing repetitive tasks by having a function call itself.
# It calls itself until it reaches base case

# Example 1:
from unittest import result


def factorial(n):
    if n < 2:
        print("Returning 1")
        return 1
    result = n * factorial(n-1)    
    print("Returning " + str(result) + " for factorial of " + str(n))
    return result
factorial(6)