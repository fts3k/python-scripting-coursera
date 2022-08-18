## print_prime_factors function. Prints all the prime factors of a number.
## A prime factor is a number that is prime & divides another without a remainder.

from unittest import result


def print_prime_factors(number):
    # Start with two
    factor = 2
    # Keep going until the factor is larger than the number.
    while factor <= number:
        # Check if the factor is a divisor of number
        if number % factor == 0:
            print(factor)
            number = number/factor
        else:
            factor += 1
    return "Done"


print_prime_factors(100)


## Question 3: Avoiding infitinite loops:

def is_power_of_two(n):
    # Check if the number can be divided by two without remainder.
    while n !=0 and n % 2 ==0:
        n = n/2
    # If after dividing by two the number is 1, it's a power of two
    if n ==1:
        return True
    return False

print(is_power_of_two(0))
print(is_power_of_two(1)) 
print(is_power_of_two(8)) 
print(is_power_of_two(9))         



### Fill isn the fucntion so that it returns the sum of all the divisors of a number, without including it - A divisor is a number that divides into another without remainder.

def sum_divisors(n):
    i = 1
    sum = 0

    # Return the sum of all divisors of n, not including it
    while i<n:
        if n%i==0:
            sum += i
        i +=1
    return sum

print(sum_divisors(0))
print(sum_divisors(3))            
print(sum_divisors(36))
print(sum_divisors(102))  


## Question 5: multiplication_table function prints the results of a number passed to it multiplied by 1 through 5.
## Additional requirement number not to exceed 25, which is done with the break statement.

def multiplication_table(number):
    # Initialize starting point of the multiplication table.
    multiplier = 1
    # Only loop through 5
    while multiplier <=5:
        result = number*multiplier
        #Additional condition to exit out of the loop?
        if result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1

multiplication_table(3)
multiplication_table(5)
multiplication_table(8)        

