#!/usr/bin/python3
"""valid UTF-8 encoding"""


def validUTF8(data):
    bytecount = 0

    for num in data:
        binary = format(num, "#010b")[-8:]
        if bytecount == 0:
            for bit in binary:
                if bit == '0':
                    break
                bytecount += 1
            if bytecount == 0:
                continue
            if bytecount == 1 or bytecount > 4:
                return False
        else:
            if binary[0] != '1' or binary[1] != '0':
                return False

        bytecount -= 1
    return bytecount == 0
