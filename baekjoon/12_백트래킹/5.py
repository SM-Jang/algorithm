# https://velog.io/@hope1213/%EB%B0%B1%EC%A4%80-9663-N-Queen-%ED%8C%8C%EC%9D%B4%EC%8D%AC
n = int(input())

graph = [0]*n
visited = [0]*n


def dfs(depth):
    global count
    if n == depth:
        count+=1
        return
    
    for i in range(n):
        if not visited[i]:
            graph[depth]=i
            t=True
            
            for j in range(depth):
                if abs(graph[depth]-graph[j]) == abs(depth-j):
                    t=False
                    break
                    
            if t:
                # print(graph, depth)
                visited[i]=1
                dfs(depth+1)
                visited[i]=0
                
count=0
dfs(0)
print(count)