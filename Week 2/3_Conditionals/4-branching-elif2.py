# The number_group function should return "Positive" if the no received is positive,
# Negative if it's negative and "Zero if it's 0"

def number_group(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

print(number_group(10))
print(number_group(0))
print(number_group(-5))
                
