# ABC136 B Uneven Numbers
# 全探索
# N以下の正の整数のうち桁数が奇数なのは？

N = int(input())
count = 0

for i in range(N):
    if len(str(i+1)) % 2 != 0:
        count += 1
        
print(count)