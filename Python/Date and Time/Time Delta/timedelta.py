#!/bin/python3

# https://www.hackerrank.com/challenges/python-time-delta/problem

# strptime() String Parse Time
# https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime

# Input:
# 2
# Sun 10 May 2015 13:54:36 -0700
# Sun 10 May 2015 13:54:36 -0000
# Sat 02 May 2015 19:54:36 +0530
# Fri 01 May 2015 13:54:36 -0000

# datetime format
#   Day dd Mon yyyy hh:mm:ss +xxxx

import sys
from datetime import datetime


dtformat = '%a %d %b %Y %H:%M:%S %z'


# Complete the time_delta function below.
def time_delta(t1, t2):
    dt1 = datetime.strptime(t1, dtformat)
    dt2 = datetime.strptime(t2, dtformat)
    return abs(int((dt1-dt2).total_seconds()))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            t = int(f.readline())
            for t_itr in range(t):
                t1 = f.readline().strip()  # strip to remove '\n'
                t2 = f.readline().strip()
                delta = time_delta(t1, t2)
                print(delta)

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # t = int(input())

    # for t_itr in range(t):
    #     t1 = input()
    #     t2 = input()
    #     delta = time_delta(t1, t2)
    #     fptr.write(delta + '\n')
    # fptr.close()
