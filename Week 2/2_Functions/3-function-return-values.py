# Example 1
from unittest import result


def area_triangle(base,height):
    return base*height/2

area_a = area_triangle(5,4)
area_b = area_triangle(6,7)
sum = area_a + area_b
print("The sum of the the two areas is:  " + str(sum))

# Example 2

def get_seconds (hours,minutes,seconds):
    return 3600*hours + minutes*60 + seconds

amount_a = get_seconds(5,7,80)
amount_b = get_seconds(54,6,7)
result = amount_a + amount_b
print(result)


# Example 3
def convert_seconds(seconds):
    hours = seconds //3600
    minutes = (seconds - hours*3600) //60
    remaining_seconds = seconds -hours*3600 - minutes*60
    return hours,minutes, remaining_seconds


convert_seconds(78900)
convert_seconds(456787)

# Function can return nothing:
def greeting(name):
    print("welcome, " + name)

result = greeting("Christine")
print(result) 


# Code reuse example

def lucky_number(name):
    number = len(name)*9
    print("Hello " + name + ". Your lucky number is " + str(number) )

lucky_number("Kay")
lucky_number("Tom")

## Code re-use example 2:
def month_days(month, days):
    print(month + " has " + str(days) + " days.")

month_days("June", 30)
month_days("July", 31)



