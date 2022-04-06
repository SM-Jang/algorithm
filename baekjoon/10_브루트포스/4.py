# 1. 입력
n,m = map(int, input().split())
chess = []
for _ in range(n):
    chess.append(input())



# 2. 8x8 체스판 유형 2가지(메모)

def check_chess_8x8(chess):
    type1='BWBWBWBW'
    type2='WBWBWBWB'
    repair1 = 0
    repair2 = 0
    
    for row in range(8):
        chess_row = chess[row]
        for col in range(8):
            chess_row_col = chess_row[col]
            if row % 2 == 0:
                if chess_row_col != type1[col]: repair1 += 1# type1
                if chess_row_col != type2[col]: repair2 += 1# type2
            else:
                if chess_row_col != type2[col]: repair1 += 1# type2
                if chess_row_col != type1[col]: repair2 += 1# type1
    return min(repair1, repair2)



# 3. 완전 탐색(수리횟수)
ans = []
for i in range(n-8+1):
    for j in range(m-8+1):
        # 8x8로 자르기
        chess_8x8 = []
        chess_rows = chess[i:i+8]
        for chess_row in chess_rows:
            chess_8x8.append(chess_row[j:j+8])

        # 고쳐야할 부분 찾기
        repair = check_chess_8x8(chess_8x8)
        
        ans.append(repair)


# 4. 최소 수리횟수 출력
print(min(ans))