def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print('Node:', v, end='\t')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]: # 인접 리스트
        if not visited[i]:
            dfs(graph, i, visited) # 같은 그래프, 다음 노드, 방문 확인

# 6까지 쭉 실행되고 아무것도 없으니 for문의 다음 노드가 나와서 다시 실행!

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
dfs(graph, 1, visited)        