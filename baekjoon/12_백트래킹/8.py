# permutation
import sys
# 0. 입력
n = int(input())
s = [[0]*n for _ in range(n)]
for i in range(n):
    s[i] = list(map(int, sys.stdin.readline().split()))
m = 1e9



def score(team):
    ans = 0
    for t1 in team:
        for t2 in team:
            ans += s[t1][t2]
            
    return ans

# 1. 팀 선정
from itertools import combinations
comb = list(combinations(range(n), n//2))
for team1, team2 in zip(comb[:len(comb)//2], sorted(comb[len(comb)//2:], reverse=True)):
    # print(team1, team2)
    
    # 2. 점수 산정
    s1, s2 = score(team1), score(team2)
    
    # 3. 계산
    if m > abs(s1-s2):
        m = abs(s1-s2)



    
print(m)



# dfs: https://developer-ellen.tistory.com/50?category=879172
def dfs(depth, idx):
    global min_diff
    # 종료 조건(팀이 다 참)
    if depth == n//2:
        power1, power2 = 0, 0
        for i in range(n):
            for j in range(n):
                # team1: visited
                if visited[i] and visited[j]:
                    power1+=graph[i][j]
                # team2: not visited
                if not visited[i] and not visited[j]:
                    power2+=graph[i][j]
        min_diff = min(min_diff, abs(power1 - power2))
        
        return
    
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False
            
n = int(input())
visited = [False for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
min_diff = int(1e9)
dfs(0,0)
print(min_diff)        