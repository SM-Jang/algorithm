def DFS(visited, node, graph):
    
    visited[node] = True
    # 이웃들
    for i in range(len(graph[node])):
        # 방문안하고 연결되어 있음
        if visited[i] == False and graph[node][i]==1:
            DFS(visited,i,graph)
            
def solution(n, computers):
    count = 0
    visited = [False] * n
    for i in range(n):
        if visited[i] == False: 
            count += 1
            DFS(visited, i, computers) # 같은 네트워크는 모두 방문 처리
            
    return count

