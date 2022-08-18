# Use in range or list 

## Another example:

def greet_friend(friends):
    for friend in friends:
        print("Hi " + friend)

greet_friend(['Taylor', 'John', 'Sammy'])
greet_friend('Barry')  # Strings are iterable so the loop will go through each letter in the string.
greet_friend(['Barry'])      # To resolve the issue above, have the string as a list.



# Common Errors in for Loops vid example:
# validate_users function used by the system to check if a list of users is valid or invalid.
# A valid user is one that is at least 3 characters long e.g ['taylor','luisa','jamaal'] are all valid users.
# 
from re import U
def is_valid(user):
    if len(user) < 3:
        return False
    elif len(user) > 15:
        return False
    else:
        return True

def validate_users(users):
    for user in users:
        if is_valid(user):
            print(user + " is valid")
        else:
            print(user + " is invalid")

validate_users(['purplecat'])