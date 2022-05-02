def dfs(n, value):
    global cnt
    if value>n:
        return
    
    for i in range(1,4):
        if value+i == n:
            cnt += 1
            return
        dfs(n, value+i)
        
# main
T = int(input())
for _ in range(T):
    n = int(input())
    cnt = 0
    dfs(n, 0)
    print(cnt)
    
    
# DP
d=[0]*15
d[1]=1
d[2]=2
d[3]=4
for i in range(4,15):
    d[i] = d[i-1]+d[i-2]+d[i-3]

# main
T = int(input())
for _ in range(T):
    n = int(input())
    print(d[n])