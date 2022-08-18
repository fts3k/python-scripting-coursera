## Qstn 3: 
# A function that return whether a number is a power of a given base.


def is_power_of(number,base):
    # Base case: when the number is smaller than base
    if number < base:
        return number ==1
    result = number//base
    # Recursive case: Keep dividing the number by base
    return is_power_of(result,base) 
    
print(is_power_of(8,2))      


## 