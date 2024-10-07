# ABC95 C - Half and Half
# 全探索
# AピザX枚BピザY枚最小何円？

A,B,C,X,Y = map(int, input().split())
price = float("inf")
for i in range(max(X,Y)+1):
    if 2*i*C + A*max(0,X-i) + B*max(0,Y-i) < price:
        price = 2*i*C + A*max(0,X-i) + B*max(0,Y-i)
    
print(price)