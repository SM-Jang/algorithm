N = int(input())
flag=False
ans = -1
# 3*x1 + 5*x2 = N
x_1, x_2 = N//3, N//5
for x2 in range(x_2, -1, -1):
    for x1 in range(x_1+1):
        y = x1*3 + x2*5
        print(x1, x2, y, N)
        if y == N:
            ans = (x1, x2)
            flag=True
            break
    if flag: break
if ans == -1: print(ans)
else: print(sum(ans))