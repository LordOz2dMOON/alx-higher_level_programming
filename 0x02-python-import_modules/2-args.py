#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv[1:]
    argv_count = len(argv)
    number = 1
    if argv_count == 0:
        print('{} arguments.'.format(argv_count))
    elif argv_count == 1:
        print('{} argument:'.format(argv_count))
        print('{}: {}'.format(number, sys.argv[1]))
    else:
        print('{} arguments'.format(argv_count))
        while number <= argv_count:
            print('{}: {}'.format(number, sys.argv[number]))
            number += 1
