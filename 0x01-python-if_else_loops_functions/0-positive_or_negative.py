#!/usr/bin/python3
import random
number = random.randint(-10, 10)

# Your code should go below this line

if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
