
#入力
N = int(input())
I = input()
S = I.split()
count = 0

for l in range(N):
    for r in range(l,N):
        if r-l == 0:
            count +=1
        elif r-l == 1:
            count +=1
            M = int(S[l])-int(S[r])
        elif int(S[r-1])-int(S[r]) == M:
            count +=1
        else:
            break

print(count)
        