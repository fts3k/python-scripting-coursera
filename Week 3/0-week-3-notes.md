Common pitfalls when using loops:

Forgetting to initialize values with the right variable.


>> Whenever you're writing a loop, check that you're initializing all the variable you want to use before you use them.


2. Avoiding Loops:
> Check your loops won't run forever.
> Initialize the variable

3. Sometimes loops are required. Provide a means to stop the loop.


while True:
    do_something_cool()
    if user_requested_to_stop():
        break



For Loops
==========
> Iterate over a sequence of values.
> for x **in** range(5):
      print(x)