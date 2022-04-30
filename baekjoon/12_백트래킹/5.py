

def dfs(x, n):
    # 종료
    global cnt
    if x >= n:
        cnt+=1
        return
    
    # x: depth
    # y: i
    for y in range(n):
        row[x] = y
        if not isused1[y] and not isused2[x+y] and not isused3[x-y+n-1]:
            isused1[y]=True
            isused2[x+y]=True
            isused3[x-y+n-1]=True
            
            dfs(x+1, n)
            
            isused1[y]=False
            isused2[x+y]=False
            isused3[x-y+n-1]=False


# main
import sys
n=int(sys.stdin.readline())
cnt = 0
isused1 = [False]*20 # 세로
isused2 = [False]*40 # 대각1
isused3 = [False]*40 # 대각2

row = [-1]*n # queen
dfs(0, n)
print(cnt)