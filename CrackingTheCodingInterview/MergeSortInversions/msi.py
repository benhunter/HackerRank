#!/bin/python3

import os
# from collections import deque
# from itertools import islice

# DEBUG = False


def merge(left: list, right: list) -> (list, int):
    arr = []
    inversions = 0
    posn_left = 0
    posn_right = 0

    # if DEBUG: print('Merge left', left, 'right', right)

    while (len(left) > posn_left or len(right) > posn_right):
        # if DEBUG: print('len(left)', len(left), 'len(right)', len(right))
        if len(left) == posn_left:
            arr.extend(right[posn_right:])
            break
        elif len(right) == posn_right:
            arr.extend(left[posn_left:])
            break
        
        # if DEBUG: print(left[0], right[0])
        # if DEBUG: print('arr', arr)

        if left[posn_left] <= right[posn_right]:
            arr.append(left[posn_left])
            posn_left += 1
        else:
            arr.append(right[posn_right])
            posn_right += 1
            inversions += len(left) - posn_left

    # if DEBUG: print('Returning arr', arr, 'inversions', inversions)
    return arr, inversions


def mergesort(arr):
    if len(arr) == 1:
        return arr, 0
    # len(arr)
    # len(arr)/2
    half = len(arr)//2
    left_arr, left_inversions = mergesort(arr[:half])
    right_arr, right_inversions = mergesort(arr[half:])

    arr, inversions = merge(left_arr, right_arr)

    return arr, (inversions + left_inversions + right_inversions)



# Complete the countInversions function below.
def countInversions(arr: list) -> int:
    count = 0
    # if DEBUG: print(arr)

    # Brute implementation, O(n^2)
    # for index, x in enumerate(arr):
    #     if DEBUG: print(index, x)
    #     for item in arr[index:]:
    #         if x > item:
    #             if DEBUG: print(x, '>', item)
    #             count += 1

    # Mergesort implementation, O(n log n)
    arr, count = mergesort(arr)


    return count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        print(result)
        # fptr.write(str(result) + '\n')

    # fptr.close()
