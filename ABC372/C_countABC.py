#C TLE

N, Q = map(int, input().split())

S = input()

for i in range(Q):
    X, C = input().split()
    S = S[:int(X)-1] + C + S[int(X):]
    print(S.count("ABC"))