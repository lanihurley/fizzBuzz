""" 
Author: Lani Hurley
Date: 4/4/22
Filename: fizzBuzz.py
The FizzBuzz Game:
    Program prints each number from 1 to 100 in turn.
    When the number is divisible by 3 then instead of printing the number it prints 'Fizz'.
    When the number is divisible by 5, then instead of printing the number it prints 'Buzz'.
    When the number is divisible by both 3 and 5 it prints 'FizzBuzz'.

"""

for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
    
