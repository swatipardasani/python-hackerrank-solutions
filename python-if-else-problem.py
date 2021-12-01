# Python If-else problem : https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())   # strip() -- removes white spaces from start and end of the string and returns the same string without white spaces | equivalent to trim()
if n % 2:
    print('Weird')
elif (n % 2 == 0) : 
    if (n >= 2 and n <= 5) : 
        print('Not Weird')
    elif (n >= 6 and n <= 20) :
        print('Weird')
    elif n > 21 : 
        print('Not Weird')
