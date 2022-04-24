import sys
# 0. 스도쿠
sudoku = [[0]*9 for i in range(9)]
Pos = [] # 공백 위치
for i in range(9):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    sudoku[i] = row
    
    for j in range(9):
        if row[j]==0: Pos.append([i,j])
        
# 가로, 세로, 사각형 확인
def availableX(row, a):
    # 행에 x가 없는지 확인
    for i in range(9):
        if sudoku[row][i] == a: 
            return False
    return True
    
def availableY(col, a):
    # 열에 x가 없는지 확인
    for j in range(9):
        if sudoku[j][col] == a: 
            return False
    return True
        
def availableRect(x, y, a):
    # 몇번째 사각형인지 확인
    nx = x//3 * 3
    ny = y//3 * 3
    # 사각형에 x가 없는지 확인
    for i in range(3):
        for j in range(3):
            if sudoku[nx+i][ny+j]==a: return False
    return True

# main: idx번째 빈칸을 처리
def dfs(idx):
    # 종료 조건
    if idx == len(Pos):
        for i in range(9):
            print(*sudoku[i])
        return
    
    # 1~9까지 하나씩 넣어보기
    for i in range(1, 10):
        x = Pos[idx][0]
        y = Pos[idx][1]
        # print(i, availableX(x, i), availableY(x, i), availableRect(x,y, i))
        if availableX(x, i) and availableY(y, i) and availableRect(x, y, i):
            sudoku[x][y] = i # 가능할 경우 놓아 보기
            dfs(idx+1) # 다음 빈칸으로 이동
            sudoku[x][y] = 0 # 끝나지 않아 돌아오면 다시 빈칸 처리
dfs(0)