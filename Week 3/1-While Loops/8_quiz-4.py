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