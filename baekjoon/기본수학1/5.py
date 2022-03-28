T = int(input())
ans = []
for _ in range(T):
    H,W,N = map(int, input().split())
    XX, YY = N//H+1, N%H
    if YY == 0:
        XX = XX-1
        YY = H
    ans.append(YY*100+XX)
for x in ans:
    print(x)