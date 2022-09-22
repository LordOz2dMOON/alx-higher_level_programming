#!/usr/bin/python3
#use a for loop to loop through 0 to 99
for i in range(0,100):
#print number with 2 digits and a comma as seperator
    if i == 99:
        print(f'{i:02}',end=" ")
        break
    print(f'{i:02}', sep= ',', end=", ")
