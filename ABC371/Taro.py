#B-Taro
#太郎?
#AC
import numpy as np

n, m = [int(i) for i in input().split()]
child = np.zeros(n) #内包表記でよかったかも

for i in range(m):
    A, B = [i for i in input().split()] #split()がリストで返すから面倒な表記にしなくてもいいじゃん
    if B == "M" and child[int(A)-1] == 0:
        print("Yes")
        child[int(A)-1] += 1
    else:
        print("No")