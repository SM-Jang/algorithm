from collections import deque

def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 시작 노드 방문 처리
    visited[start] = True
    
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에 가장 먼저 들어와 있는 노드
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            # 인접 노드들
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                


# 인접 리스트!!            
graph = [
    [],
    [2,3,8], # 1번 노드와 연결되어 있는 인접 노드
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현
visited = [False]*9

# 1번 노드부터 시작
bfs(graph, 1, visited)    