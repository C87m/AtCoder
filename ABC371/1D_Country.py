#D-1D country
#TLE　
'''
N = int(input())
X = [int(i) for i in input().split()]
P = [int(i) for i in input().split()]
Q = int(input())

for i in range(Q):
    total = 0
    L, R = [int(i) for i in input().split()]
    for j in range(len(X)):
        if L <= X[j] and X[j] <= R:
            total += P[j]
    print(total)
'''