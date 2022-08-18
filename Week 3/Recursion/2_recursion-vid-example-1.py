# sum_positive function should return the sum of all positive numbers btn number n received and 1.
# For example, when n is 3 it should return 1+2_3=6 

def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return n
    # The recursive case is adding this number to the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n-1)


print(sum_positive_numbers(3))
print(sum_positive_numbers(13))
