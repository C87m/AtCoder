# B 1Dkeybord
#移動距離
# AC

S = input()
x = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = S.index("A")
count = 0

for i in range(25):
    count += abs(S.index(x[i+1])-key)
    key = S.index(x[i+1])
    
print(count)