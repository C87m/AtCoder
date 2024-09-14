#A-Jiro
#次男は誰？
#AC

S_ab, S_ac, S_bc = [i for i in input().split()]

if S_ab != S_ac:
    print("A")
elif S_ac != S_bc:
    print("C")
else:
    print("B")