
# Introducing use of if
def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be atleast 3 characters long")
    else:
        print("Valid Username")


# The is_positive function should return True if the no received is positive. Otherwise it returns no.

def is_positive(number):
    if number > 0:
        return True
    else:
        return None    

## or
def is_positive(number):
    if number > 0:
        return True
    return None

is_positive(5)
is_positive(-4)
