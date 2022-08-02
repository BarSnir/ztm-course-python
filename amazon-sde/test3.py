#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countFamilyLogins' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY logins as parameter.
#

letter_dict = {
    "a": "b",
    "b": "c",
    "c": "d",
    "d": "e",
    "e": "f",
    "f": "g",
    "g": "h",
    "h": "i",
    "i": "j",
    "j": "k",
    "k": "l",
    "l": "m",
    "m": "n",
    "n": "o",
    "o": "p",
    "p": "q",
    "q": "r",
    "r": "s",
    "s": "t",
    "t": "u",
    "u": "v",
    "v": "w",
    "w": "x",
    "x": "y",
    "y": "z",
    "z": "a",
}

def countFamilyLogins(logins) -> int:
    global letter_dict
    pairs_count = 0
    for login_code in logins:
        converted_code = ''.join([letter_dict.get(letter) for letter in login_code])
        if converted_code in logins: 
            pairs_count = pairs_count + 1
    return pairs_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    logins_count = int(input("Please enter logins count: ").strip())

    logins = []

    for _ in range(logins_count):
        logins_item = input("Please put single unit code: ")
        logins.append(logins_item)

    result = countFamilyLogins(logins)
    fptr.write(str(result) + '\n')

    fptr.close()
