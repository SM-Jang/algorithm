def neighbor(w1, w2):
    n = len(w1)
    cnt = 0 
    for i in range(n):
        if w1[i] != w2[i]: cnt += 1
    
    if cnt == 1: return True
    else: return False
    

    
    
    
    
import heapq
def solution(begin, target, words):
    depth=0
    if target not in words: return depth

    q = []
    heapq.heappush(q, (depth, begin))
    
    while q:
        # bfs
        depth, word = heapq.heappop(q)
        depth += 1

        for w in words:
            if neighbor(word, w):
                if w != target:
                    heapq.heappush(q, (depth, w))
                else: return depth
                
                
