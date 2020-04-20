# Merge the Tools!
# https://www.hackerrank.com/challenges/merge-the-tools/problem

import sys

def merge_the_tools(s, k):
    for i in range(len(s) // k):
        start = i * k
        end = start + k
        t = s[start:end]
        print(remove_dups(t))


def remove_dups(t):
    u = ''
    for c in t:
        if c not in u:
            u += c
    return u


if __name__ == '__main__':
    # print(sys.argv)
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            string = f.readline()
            k = int(f.readline())
    else:
        string, k = input(), int(input())
    merge_the_tools(string, k)
