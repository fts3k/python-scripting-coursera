# sum_squares function that returns the sum of all the squares of numbers btn 0 to x (not included).
# You can use the range(x) function to generate a sequence of numbers from 0 to x (not included)

def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n) 
    return sum

print(sum_squares(10)) 
print(sum_squares(30))         


## Example 2

values = [23,52,59,37,48]
sum = 0
length = 0

for value in values:
    sum += value
    length += 1

print("Total sum: " + str(sum) + " - Average: " + str(sum/length))


## Some of the areas you can use for loops
# 1. Copy Files to Machines.
# 2. Process the contents of files.
# 3. Automatically install SW

# Use for loops when there's a sequence of elements that you want to iterate.
# Use while loops when you want to repeat action until condition changes.

