#!/usr/bin/python3
#write a function with prototype: def fizzbuzz():
def fizzbuzz():
#for loop that traverses numbers from 1 to 100
    for i in range(1,101):
#check if number is divisible by both 3 and 5
        if(i%3==0 and i%5==0):
            print("FizzBuzz", end = ' ')
#check if number is divisible by 3
        elif(i%3 == 0):
            print("Fizz", end = ' ')
#check if number is divisible by 5
        elif(i%5 == 0):
            print("Buzz", end = ' ')
#if not divisible by either of them print the i
        else:
            print(i, end = ' ')

fizzbuzz()
