from collections import deque



def bfs(n):
    
    q = deque()
    q.append((0, n)) # (depth, node)
    
    while True:
        depth, n = q.popleft()
        if n==1: return depth
        
        # neighbor
        depth += 1
        if n%3==0:
            q.append((depth, n//3))
        if n%2==0:
            q.append((depth, n//2))
        q.append((depth,n-1))


# main
n = int(input())
cnt = bfs(n)
print(cnt)
