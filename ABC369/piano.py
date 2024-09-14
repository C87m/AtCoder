
def piano(A, S, L, R, tired):
    if S == "L":
        if L != 0:#初期位置じゃない
            tired += abs(A-L)
    
        
    if S == "R":
        if R != 0:#初期位置じゃない
            tired += abs(A-R)
            
    return tired
            
    

#入力
#鍵盤をたたく回数
N = int(input())
L = 0
R = 0
tired = 0

for i in range(N):
    I = input()
    A = int(I.split()[0])
    S = I.split()[1]
    tired = piano(A, S, L, R, tired)
    if S == "L":
        L = A
    else:
        R = A

print(tired)
