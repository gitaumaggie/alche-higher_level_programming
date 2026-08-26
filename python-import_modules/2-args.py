#!/usr/bin/python3

from sys import argv


if __name__ == "__main__":
    number = len(argv) - 1

    if number == 0:
        print("0 arguments.")
    elif number == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(number))

    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
