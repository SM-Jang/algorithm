from collections import deque

def check(s1, s2):
    """
    1개만 다르면 True
    else: False
    """
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]: count+=1
        
    if count == 1: return True
    else: return False


def solution(begin, target, words):
    if not target in words: return 0
    
    visited = {}
    for w in words:
        visited[f'{w}'] = False
    
    
    q = deque()
    depth = 0
    q.append((begin, depth))
    
    while q:
        now, depth = q.popleft()
        if now == target: return depth
        
        for word in words:
            if check(now, word) and not visited[word]:
                q.append((word, depth+1))
                
    return depth
                
        
        
        
        
solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
        