# John Sullivan & Shane Wallerick
# marriage.py
# CSC440
# 1/30/2020

import sys

def tests():
    args = str(sys.argv)
    print(args)


def Marriage(args):
    dataFile = open(args[1], "r")
    line = dataFile.readline()
    while line:
        print(line)
        line = dataFile.readline()

def main():
    args = str(sys.argv)
    Marriage(args)


main()
