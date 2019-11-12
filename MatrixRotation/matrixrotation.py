#!/bin/python3

import math
import os
import random
import re
import sys

from collections import deque
from copy import deepcopy


DEBUG = True

# Complete the matrixRotation function below.
def matrixRotation(matrix, rotations):

    rows = len(matrix)
    columns = len(matrix[0])

    if DEBUG:
        print(matrix)
        print(rotations)
        print("rows", rows)
        print("columns", columns)

    # make rings
    rings = deque([])

    # how many rings?
    num_rings = min(rows, columns) // 2

    for current_ring in range(num_rings):
        if DEBUG: print('ring', current_ring)

        rings.append(deque([]))

        start_pos = {'row': current_ring, 'column': current_ring}
        if DEBUG: print(' start pos', start_pos)

        down = rows - (current_ring * 2)
        if DEBUG: print(' down', down)
        
        right = columns - (current_ring * 2)
        if DEBUG: print(' right', right)

        # down
        if DEBUG: print('   down')
        for i in range(down):
            current_row = start_pos['row'] + i
            current_column = start_pos['column']
            rings[current_ring].append(matrix[current_row][current_column])
            if DEBUG: print('  ', current_row, current_column, matrix[current_row][current_column])
        
        # right
        if DEBUG: print('   right')
        for i in range(right - 1):
            current_row = start_pos['row'] + down - 1
            current_column = start_pos['column'] + i + 1
            rings[current_ring].append(matrix[current_row][current_column])
            if DEBUG: print('  ', current_row, current_column, matrix[current_row][current_column])
        
        # up
        if DEBUG: print('   up')
        for i in range(down - 1):
            current_row = start_pos['row'] + down - 2 - i
            current_column = start_pos['column'] - 1 + right
            rings[current_ring].append(matrix[current_row][current_column])
            if DEBUG: print('  ', current_row, current_column, matrix[current_row][current_column])

        # left
        if DEBUG: print('   left')
        for i in range(right - 2):
            current_row = start_pos['row']
            current_column = start_pos['column'] - 2 + right - i
            rings[current_ring].append(matrix[current_row][current_column])
            if DEBUG: print('  ', current_row, current_column, matrix[current_row][current_column])

    if DEBUG: print(rings)

    # rotate each ring
    for ring in rings:
        rots = rotations % len(ring)
        for i in range(rots):
            ring.append(ring.popleft())
    if DEBUG: print(rings)

    # output
    rot_rings = deepcopy(rings)

    for count, ring in enumerate(rings):
        if DEBUG: print(count, ring)
        



if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])  # rows

    n = int(mnr[1])  # columns

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
