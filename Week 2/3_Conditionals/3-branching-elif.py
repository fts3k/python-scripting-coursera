from re import U


def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    elif len(username) > 15:
        print("Invalid username. Cannot be longer than 15 characters")
    else:
        print("Valid username") 

hint_username("er")
hint_username("tyiitjhdsdhs")
hint_username("ffjfdjfeidjfhdsjaiwihthdjddjsjfddsjsjdjd")
