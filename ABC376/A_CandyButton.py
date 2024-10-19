#ABC376 A - Candy Button
# あめ何個もらえる？

N, C = map(int, input().split())
T = list(map(int, input().split()))

candy = 1
t = T[0]
for i in range(1,len(T)):
    if T[i]-t >= C:
        candy += 1
        t = T[i]
        
print(candy)