# ABC68 B Break Number
# 全探索
# 2で割れる回数が多いものは？

N = int(input())
max_count = 0
max_number = 1

for i in range(1,N+1):
    count = 0
    j = i
    while j % 2 == 0:
        count += 1
        j /= 2
    if count > max_count:
        max_count = count
        max_number = i
        
print(max_number)