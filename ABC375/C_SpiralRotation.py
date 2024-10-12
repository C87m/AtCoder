# C - Spiral Rotation
# 塗り替え
# わかんなかった

N = int(input())

grid = []
for i in range(N):
    grid.append(list(input()))

for i in range(N//2):
    for x in range(i,N-i):
        for y in range(i, N-i):
            grid[y][N-x-1] = grid[x][y]

ans = []
for i in range(N):
    print("".join(grid[i]))