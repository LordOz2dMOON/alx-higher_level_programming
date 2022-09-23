#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv[1:]
    argv_count = len(argv)
    number = 1
    if argv_count is 0:
        print('{:d} arguments.'.format(argv_count))
    elif argv_count is 1:
        print('{:d} argument:'.format(argv_count))
        print('{:d}: {:s}'.format(number, sys.argv[1]))
    else:
        print('{:d} arguments:'.format(argv_count))
        while number <= argv_count:
            print('{:d}: {:s}'.format(number, sys.argv[number]))
            number += 1
