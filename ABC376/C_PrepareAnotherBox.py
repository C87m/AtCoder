# C - Prepare Another Box
import heapq

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A_minus = list(map(lambda x: x*(-1), A))
B_minus = list(map(lambda x: x*(-1), B))
heapq.heapify(A_minus)
heapq.heapify(B_minus)

x = float("inf")
flag = 1
while A_minus:
    if len(B_minus)==0:
        x = A_minus[0] * (-1)
        break
    maxA = heapq.heappop(A_minus)
    maxB = heapq.heappop(B_minus)
    if maxA < maxB:
        flag -= 1
        if flag == -1:
            break
        x = maxA*(-1)
        heapq.heappush(B_minus,maxB)
    
    
if flag == -1:
    print(-1)
else:
    print(x)