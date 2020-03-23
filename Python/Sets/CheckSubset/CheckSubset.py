
if __name__ == '__main__':
    t = int(input())
    
    for test in range(t):
        input()
        A = set(map(int, input().split()))
        input()
        B = set(map(int, input().split()))

        print(A.issubset(B))
