n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input(f'{i+1}번째 행 입력:'))))
    
# stack

def dfs(x,y):
    """
    (x,y): 그래프에서 현 위치
    """
    # 그래프 범위 밖
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False 
    
    
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y]=1
        # 상,하,좌,우 채크
        # True and False를 return하지만 결국 그냥 
        # graph[x][y] 채크 외에는 return으로 어떠한 자극도 없음
        dfs(x-1,y) 
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    
    return False
        
        
result = 0
for i in range(n):
    for j in range(m):
        # print(f'({i}, {j})')
        if dfs(i,j)==True:
            result+=1

print(result)