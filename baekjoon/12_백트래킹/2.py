# 입력
n,m = map(int, input().split())


def dfs(visited, i, n, max_depth):
    # 1. stack에 담기
    visited[i] = True
    
    # 2. 판별: 스택의 깊이가 max_depth이면 종료, pop
    if sum(visited) == max_depth:
        for i,v in enumerate(visited):
            if v: print(i+1, end=' ')
        print()
        return visited
    
    # 3. 추가: stack없는 것들 담기
    for node in range(n):
        # 방문 안하고 오름차순만 고려
        if not visited[node] and node > i:
            visited = dfs(visited, node, n, max_depth)
            visited[node]=False 

    return visited



for i in range(n):
    visited = [False]*n # stack으로 사용
    dfs(visited, i, n, m)
    