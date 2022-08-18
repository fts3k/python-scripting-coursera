# Qstn 1: Print number 1 thro 7

number = 1
while number <= 7:
    print(number, end=" ")
    number +=1


# Qsnt 2: Function to print out each letter in a separate line.
# 
def show_letters(word):
    for letter in word:
        print(letter)

show_letters("Hello")        


# Qstn 3; Function that returns how many digits the number has.
import math

def digits(n):
    count = 0
    if n== 0:
        return 1
    while (n>0):
        count +=1    
        n = math.floor(n/10)
    return count

print(digits(25))        