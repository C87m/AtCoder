# ABC133 B Good Distance
# 全探索
# D次元空間上のN個の点　i番目とj番目の点の距離が整数となる組合せはいくつ？

import math

N, D = map(int, input().split())
count = 0
X = []
for i in range(N):
    X.append(list(map(int, input().split())))

for i in range(N):
    for j in range(i+1,N):
        if math.sqrt(sum([(a-b)**2 for a,b in zip(X[i],X[j])])) % 1 == 0:
            count += 1
            
print(count)