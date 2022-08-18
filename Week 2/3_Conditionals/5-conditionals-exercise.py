# Question 1
print(2**2 ==4)

# Question 2: Function receives a name, then returns a greeting based on whether or not the name is Taylor

def greeting(name):
    if name == "Taylor":
        return "Welcome back Taylor"
    else:
        return "Hello there, " + name 
print(greeting("Taylor"))
print(greeting("John")) 

# Question 3: Output if number equals 10:

def calculate(numero):
    if numero > 11:
        print(0)
    elif numero != 10:
        print(1)
    elif numero  >= 20 or numero < 12:
        print(2)
    else:
        print(3)

calculate(10)            

# Question 4
print("A dog" < "A mouse")
print( 9999+8888 < 100*100)
print( 9999+8888 > 100*100)

# Question 5: Calculating filesystem block storage capacity

def calcutate_storage(filesize):
    block_size = 4096
    full_blocks = filesize//block_size
    partial_block_remainder = filesize%block_size
    if partial_block_remainder > 0:
        return block_size*(full_blocks+1)
    return full_blocks*block_size

print(calcutate_storage(1))
print(calcutate_storage(4096))
print(calcutate_storage(4097))
print(calcutate_storage(6000))
