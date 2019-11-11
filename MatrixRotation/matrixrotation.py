#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matrixRotation function below.
def matrixRotation(matrix, rotations):
    print(matrix)
    print(rotations)

    rows = len(matrix)
    columns = len(matrix[0])

    print("rows", rows)
    print("columns", columns)

    # make rings
    rings = []
    rings.append([])

    # how many rings?
    num_rings = min(rows, columns) // 2

    for current_ring in range(num_rings):
        start_pos = {'row': current_ring, 'column': current_ring}
        print(' start pos', start_pos)

        down = rows - (current_ring * 2)
        print(' down', down)
        
        right = columns - (current_ring * 2)
        print(' right', right)

        # down
        print('   down')
        for i in range(down):
            # print(i)
            print('  ', start_pos['row'] + i, start_pos['column'])
        
        # right
        print('   right')
        for i in range(right - 1):
            print('  ', start_pos['row'] + down - 1, start_pos['column'] + i + 1)
        
        # up
        print('   up')
        for i in range(down - 1):
            print('  ', start_pos['row'] + down - 2 - i, start_pos['column'] - 1 + right)

        # left
        print('   left')
        for i in range(right - 2):
            print('  ', start_pos['row'], start_pos['column'] - 2 + right - i)


    # rotate each ring

    # output

if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])  # rows

    n = int(mnr[1])  # columns

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
