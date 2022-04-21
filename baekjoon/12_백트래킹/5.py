def check(row):
    for i in range(row):
        # 2-1. 현 queen의 위치 (열)이 이전에 놓은 것과 겹치는 지(행은 절대 안겹침)
        # 2-2. 대각으로 겹치는지
        if qPos[row] == qPos[i] or abs(qPos[row]-qPos[i]) == (row-i):
            return False
    return True


def dfs(depth):
    global cnt
    # 종료 조건
    if depth >= n: 
        cnt += 1
        return
    
    for i in range(n):
        # 1. 위치에 퀸 놓기
        qPos[depth] = i
        
        # 2. 가능 위치 확인
        if check(depth):
            dfs(depth+1)


# main
n=int(input())
cnt = 0
qPos = [-1] * n # (index, value) = (행, 열)
dfs(0)
    
print(cnt)