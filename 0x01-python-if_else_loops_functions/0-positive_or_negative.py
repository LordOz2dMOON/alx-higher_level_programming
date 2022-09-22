#!/usr/bin/python3
import random
number = random.randint(-10, 10)
#if the number is greater than 0: print the number is positive
if number is > 0:
    print(f'{number} is positive')
#if the number is 0:print the number is zero
elif number == 0:
    print(f'{number} is zero')
#if the number is less than 0: print the number is negative
elif number < 0:
    print(f'{number} is negative')
