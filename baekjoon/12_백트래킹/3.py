n, m = map(int , input().split())

# dfs
def dfs(stk, node, n, m):
    
    # 1. push
    stk.append(node)
    
    # 2. 스텍이 가득 찼는지?
    if len(stk)==m:
        # print("출력:",stk)
        for i in stk:
            print(i, end=' ')
        print()
        stk.pop() # pop
        return stk
    
    
    # 3. 다음 노드 확인
    for i in range(1, n+1):
        # print(f'Cur {node} Next {i} stk {stk}')
        stk = dfs(stk, i, n, m)
    
    # 4. level간 이동
    stk.pop()
    return stk
        
for i in range(1, n+1):
    stk = []
    dfs(stk, i, n, m)
    