## Question Two:
# factorial function return the factorial of n.
# Then print the first 10 factorials (from 0 to 9) with the corresponding number.



def factorial(n):
    result = 1
    for x in range(1,n+1):
        result = result * x
    return result

for n in range(1,10):
    print(n,factorial(n+1))



### Qstn 3: Write script that prints the first 10 cube numbers (x**3) starting with x=1 and ending with x=10

for x in range(1,10):
    result = x**3
    print(result)


## Qstn 4: Script that prints the multiples of 7 btn 0 to 100.
# Print one multiple per line and avoid printing any numbers that aren't multiples of 7.

for n in range(0,100):
    if n != 0 and n%7 == 0:
        print(n)   


## Qstn 5: Retry function tries to execute an operation that might fail, it retries the operation for a number of attempts.
# Currently the code will keep executing the function even if it succeeds.
# # Write a code to stops trying after the operation succeeds.
# 
def retry(operation, attempts):
    for n in range(attempts):
        if operation():
            print("Attempt " + str(n) + " succeeded")
            break
        else:
            print("Attempt " + str(n) + " failed")

# retry(create_user, 3)     ## This two won't execute because I don't have access to the functions defined.
# retry( stop_service, 5)                    

