#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in November 2020
# Program finding circumference and area of a circle


import math


def main():
    rad = 15
    circ = math.pi*2*rad
    area = math.pi*rad**2
    print("The circumference of a circle with a radius of 15mm is:")
    print("{}mm".format(circ))
    print("The area of a circle with a radius of 15mm is::")

    # https://codeigo.com/python/printing-subscript-and-superscript
    superscript = str.maketrans("2", "²")
    print("{}mm2".translate(superscript).format(area))


if __name__ == "__main__":
    main()
