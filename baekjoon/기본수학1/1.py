A, B, C = map(int , input().split())

if (C-B)<=0: print(-1)
else:
    x = A//(C-B)+1

    if x < 0: print(-1)
    else: print(x)