#!/usr/bin/python3
#create a function with prototype def uppercase(str):
def uppercase(str):
#create an empty string
    uppercase = ''
#loop through the string 'str' with a for loop
    for i in str:
#check if the current letter is a small letter with ord()
        if ord(i) >= 97 and ord(i) <= 122:
#if yes then, save the current number with its unicode value
            i = ord(i)
#after saving minus 32 to get the capital equivalent unicode number
            i -= 32
#use chr() to get the capital letter of the unicode value
            i = chr(i)
#add letter to empty string
            uppercase = uppercase + i
#check if letter is a big letter and also add to uppercase string
        elif ord(i) >= 65 and ord(i) <= 90:
            uppercase = uppercase + i
#check for all others and also add to uppercase string
        else:
            uppercase = uppercase + i
#print new uppercase string
        print(uppercase, end='\n')
