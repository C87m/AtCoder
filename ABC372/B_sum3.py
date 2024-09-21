#B 3^A WA

M = int(input())
N = 0
A = []


for i in range(20):
    N += 1
    M2 = M
    A.append(0)
    if M % 3 == 0:#3で割り切れるなら割り続ける
        A[i] +=1
        M2 /= 3
        while M2 % 3 == 0:
            A[i] +=1
            M2 /= 3
            if A[i] == 9:
                break
        M -= 3**A[i]
    else:
        A[i] = 0
        M -= 1
    if M == 0:
        break

            
print(N)
print(*A)
            