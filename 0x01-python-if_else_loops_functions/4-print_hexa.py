#!/usr/bin/python3
#use a for loop to range through 0 to 98
for i in range(99):
#in the loop check for the hexadecimal of the current number
    hex_no = hex(i)
#print the number and hexadecimal with format number = hexadecimal
    print(f'{i} = {hex_no}')
