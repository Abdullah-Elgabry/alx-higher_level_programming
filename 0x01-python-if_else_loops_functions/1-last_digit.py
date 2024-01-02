#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
result = number % 10 if number > 10 else number % -10
print(f"Last digit of {number:d} is {result:d} and is", end=" ")
if result > 5:
    print("greater than 5")
elif result == 0:
    print("0")
else:
    print("less than 6 and not 0")
