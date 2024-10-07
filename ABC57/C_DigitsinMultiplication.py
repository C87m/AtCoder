# ABC57 C - Digits in Multiplication
# 全探索
# F(A,B)桁数の多い方　N=A*BのときのF(A,B)の最小値

N = int(input())
minF = 10000

def F(a, b):
    return max(len(str(a)), len(str(b)))

for i in range(1,100000):
    if N % i == 0:
        minF = min(minF,F(i,N//i))
        
print(minF)