# B - Hands on Ring (Easy)
# ハンドル移動

N, Q = map(int, input().split())

loc_L = 1
loc_R = 2

count = 0
for i in range(Q):
    S = input().split()
    H = S[0]
    T = int(S[1])
    
    if H == "L":
        if loc_L < loc_R and loc_R < T:
            count += loc_L + N - T
        elif loc_L < T and T < loc_R:
            count += T - loc_L
        elif T < loc_L and loc_L < loc_R:
            count += loc_L - T
        elif T < loc_R and loc_R < loc_L:
            count += T + N - loc_L
        elif loc_R < loc_L and loc_L < T:
            count += T- loc_L
        else:
            count += loc_L - T
        loc_L = T
    else:
        if loc_R < loc_L and loc_L < T:
            count += loc_R + N - T
        elif loc_R < T and T < loc_L:
            count += T - loc_R
        elif T < loc_R and loc_R < loc_L:
            count += loc_R - T
        elif T < loc_L and loc_L < loc_R:
            count += T + N - loc_R
        elif loc_L < loc_R and loc_R < T:
            count += T- loc_R
        else:
            count += loc_R - T
        loc_R = T

print(count)
    