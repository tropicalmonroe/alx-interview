#!/usr/bin/python3

""" a script that reads stdin line by line and computes metrics"""

import sys

def printstate(disc, size):
    """info print"""
    print("File size: {:d}".format(size))
    for x in sorted(disc.keys()):
        if disc[x] != 0:
            print("{}: {:d}".format(x, disc[x]))

# sourcery skip: use-contextlib-suppress
statuscode = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
              "404": 0, "405": 0, "500": 0}

count = 0
size = 0

try:
    for line in sys.stdin:
        if count != 0 and count % 10 == 0:
            printstate(statuscode, size)

        stlist = line.split()
        count += 1

        try:
            size += int(stlist[-1])
        except Exception:
            pass

        try:
            if stlist[-2] in statuscode:
                statuscode[stlist[-2]] += 1

            except Exception:
                pass
        printstate(statuscode, size)

except KeyboardInterrupt:
    printstate(statuscode, size)
    raise
