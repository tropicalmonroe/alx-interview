#!/usr/bin/python3
"""
data set represents a valid UTF-8 encoding
"""

def validUTF8(data):
    """
    Data: int li
    Return: True if data is a valid UTF-8 encoding, else return False
    encoding, else return False
    """

    bytecount = 0

    for x in data:
        if bytecount == 0:
            if x >> 5 == 0b110 or x >> 5 == 0b1110:
                bytecount = 1
            elif x >> 4 == 0b1110:
                bytecount = 2
            elif x >> 3 == 0b11110:
                bytecount = 3
            elif x >> 7 == 0b1:
                return False
        else:
            if x >> 6 != 0b10:
                return False
            bytecount -= 1
        return bytecount == 0
