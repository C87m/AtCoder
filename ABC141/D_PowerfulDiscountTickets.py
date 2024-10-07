# ABC141 D Powerful Discount Tickets
# heapqの練習

import heapq

N, M = map(int, input().split())

prices = list(map(lambda x: int(x) *(-1), input().split()))
    
heapq.heapify(prices)

for i in range(M):
    max = heapq.heappop(prices) 
    heapq.heappush(prices,(-1)*(-max//2))
    
print(-sum(prices))