# n, m = 5, 6
n, m = map(int, input().split())
# graph = [ [1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
graph = []
graph.append([0]*n)
for _ in range(n):
    graph.append(list(map(int, input())))
    
# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# bfs -> queue
from collections import deque
def bfs(x, y):
    """
    0: 괴물
    else: 통과 가능
    """
    # 시작 위치
    queue = deque()
    queue.append((x, y))
    
    while queue:
        # 현재 노드
        x, y = queue.popleft()
        for i in range(4):
            # 이동 후 새 위치
            nx = x+dx[i]
            ny = y+dy[i]
            
            # 새 위치가 범위 밖이면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            
            # 새 위치에 몬스터 있으면 무시
            if graph[nx][ny] == 0: continue
            
            if graph[nx][ny] == 1:
                # 이동할 위치
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                if nx==(n-1) and ny ==(m-1): return graph


            
        
        
        
    
    

    
graph = bfs(0,0)
print(graph[n-1][m-1])