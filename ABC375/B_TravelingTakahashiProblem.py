# B - Traveling Takahashi Problem
# 移動コスト
import math

N = int(input())

cost = 0
X0 = 0
Y0 = 0
for i in range(N):
    X, Y = [int(j) for j in input().split()]
    cost += math.sqrt((X0-X)**2+ (Y0-Y)**2)
    X0, Y0 = X, Y
    
cost += math.sqrt(X**2+Y**2)

print(cost)
    