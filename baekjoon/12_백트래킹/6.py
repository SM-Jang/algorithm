# https://hongcoding.tistory.com/118
import sys
graph = []
blank = []
# sudoku
for i in range(9):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 공백 위치
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i, j))

# 가로, 세로, 사각형 확인
def checkRow(x, a):
    for i in range(9):
        if a == graph[x][i]:
            return False
    return True

def checkCol(y, a):
    for i in range(9):
        if a == graph[i][y]:
            return False
    return True

def checkRect(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == graph[nx+i][ny+j]:
                return False
    return True

# main: idx번째 공백에 숫자를 넣으며 확인
def dfs(idx):
    if idx == len(blank):
        for i in range(9):
            print(*graph[i])
        exit(0)
    # idx번째 x,y의 공백위치에 1~9를 넣으며 확인
    for i in range(1, 10):
        x = blank[idx][0]
        y = blank[idx][1]

        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):
            graph[x][y] = i
            dfs(idx+1)
            graph[x][y] = 0

dfs(0)