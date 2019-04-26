# Using the built-in functions on Numbers perform following operations

import math
import random

number = 1.780838373

# a) Round of the given floating point number. Example:
# n=0.543 then round it next decimal number, i.e n=1.0 Use round() function
print(round(number))

# b) Find out the square root of a given number. (Use sqrt(x) function)
print(math.sqrt(number))

# c) Generate random number between 0, and 1 ( use  random() function)

for i in range(10):
    print(random.random(), end=" ")

print("\n")
print("*" * 100)

# d) Generate random number between 10 and  500. (Use uniform() function)

for i in range(10):
    print(random.uniform(10, 500), end=" ")

print("\n")
print("*" * 100)

# e) Explore all Math and Random module functions on a given number/List.

print(math.ceil(number))
print(math.floor(number))
print(math.factorial(4))
print(math.exp(2))
print(math.sin(45))

print(random.randint(1, 100))
random.seed(7)
print(random.random())
random.seed(9)
print(random.random())
random.seed(7)
print(random.random())
random.seed(9)
print(random.random())

li = [1, 4, 5, 10, 2]
print(li)
random.shuffle(li)
print(li)
