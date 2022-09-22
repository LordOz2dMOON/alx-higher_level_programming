#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
#get the last digit of number and store in a variable last_digit
last_digit = number % 10
#if the last digit of number is greater than 5, print 'last digit of number is last_digit and is greater than 5'
if last_digit > 5:
    print(f'Last digit of {number} is {last_digit} and is greater than 5')
#if the last digit of number is 0, print 'last digit of number is last_digit and is 0'
elif last_digit == 0:
    print(f'Last digit of {number} is {last_digit} and is 0')
#if the last digit of number is less than 6 and not 0, print 'last digit of number is last_digit and is less
#than 6 and not 0'
elif (last_digit < 6 and != 0):
    print(f'Last digit of {number} is {last_digit} and is less than 6 and not 0')
