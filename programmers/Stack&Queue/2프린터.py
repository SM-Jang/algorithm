from collections import deque
def solution(priorities, location):
    ans = []
    q = [(i,p) for i, p in enumerate(priorities)]
    q = deque(q)

    while q:
        i,p = q.popleft()
        # print((i,p), ans, q)
        M = 0
        for _, prior in q:
            if M < prior: M=prior

        if p >= M: ans.append(i)
        else: q.append((i,p))


    return ans.index(location) + 1
