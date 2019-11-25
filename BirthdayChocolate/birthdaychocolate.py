#!/bin/python3

# https://www.hackerrank.com/challenges/the-birthday-bar/problem

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    # print(s)
    # print(d)
    # print(m)
    total = d
    length = m
    count = 0

    for pos in range(len(s) - length + 1):
        test_sum = sum(s[pos:pos + length])
        if test_sum == total:
            # print('Found position', pos, 'to', pos + length)
            count += 1
    return count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
