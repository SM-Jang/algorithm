# 1. 입력
n, m = map(int, input().split())


# 3. dfs
def dfs(stk, sup, max_depth):
    # 3-1. push
    stk.append(sup)
    
    # 3-2. 종료 채크
    if len(stk) == max_depth:
        # print(stk)
        for x in stk:
            print(x, end=' ')
        print()
        return stk
    
    # 3-3. 자식 노드 탐색
    for sub in range(1, n+1):
        if sup > sub: continue # 제약 조건: 비 내림차순
        # 깊이 우선 탐색
        stk = dfs(stk, sub, max_depth)
        stk.pop()
    return stk
        

# 2. init node를 반복으로 진행
for init in range(1, n+1):
    stk = [] # stack
    dfs(stk, init, m)
    