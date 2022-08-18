
# Question 1:
   ## Function that converts miles to kilometres

from email import message


def convert_distance(miles):
    km = miles*1.6
    return km

my_trip_miles = 55
my_trip_km = convert_distance(my_trip_miles)
print("The distance in kilometers is " + str(my_trip_km))
print("The round-trip in kilometers is " + str(my_trip_km*2))


# Question 2 - Return numbers in increasing order.

def order_numbers(number1, number2):
    if number2 > number1:
        return number1, number2
    else:
        return number2, number1

smaller, bigger = order_numbers(100,99)
print(smaller,bigger)


# Question 3 - Lucky Number

def lucky_number(name):
    number = len(name) * 9
    message = "Hello " + name + ". Your lucky number is " + str(number)
    return message

print(lucky_number("Kay"))
print(lucky_number("Cameron"))

