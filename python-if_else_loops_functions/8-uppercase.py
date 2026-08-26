#!/usr/bin/python3


def uppercase(str):
    for c in str:
        print("{:c}".format(
            ord(c) - 32 if 97 <= ord(c) <= 122 else ord(c)), end="")
    print()
