# 1. 입력(체스판) -> 2차원 행렬
row, col = map(int, input().split())
chess = []
for _ in range(row):
    chess.append(input()) # 문자열 입력
    
# 8x8씩 확인
repair = []
for r in range(row-7):
    for c in range(col-7):
        # 2. 시작 색 확인
        init1=0 #'W'
        init2=0 #'B'
        for i in range(r, r+8):
            for j in range(c, c+8):
                # 2. 시작 색 확인
                if (i+j) % 2 == 0:
                    if chess[i][j] != 'W': init1+=1
                    if chess[i][j] != 'B': init2+=1
                else:
                    if chess[i][j] != 'W': init2+=1
                    if chess[i][j] != 'B': init1+=1
        repair.append(min(init1, init2))
        
print(min(repair))