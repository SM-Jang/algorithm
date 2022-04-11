import sys
from itertools import permutations
n, m = map(int, sys.stdin.readline().split())

memo = list(range(1, n+1))
for case in list(permutations(memo,m)):
    for c in case:
        print(c, end=' ')
    print()
    
#############


visited = [False]*n
out = []

def dfs(depth, n, m):
    if depth == m:
        print(' '.join(map(str, out)))
        return
    for i in range(len(visited)):
        if not visited[i]:
            visited[i]=True
            
            out.append(i+1)
            dfs(depth+1, n, m)
            
            visited[i]=False
            out.pop()
            
dfs(0,n,m)