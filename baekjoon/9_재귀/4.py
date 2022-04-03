# a는 현재 n개의 원판이 쌓여있는 곳, 
# b는 n-1개의 원판을 옮겨 놓을 곳, 
# c는 a에서 남은 원판을 놓을 곳이 된다.
def hanoi(n, a, b, c):
    if n==1:
        move.append([a,c])
    else:
        hanoi(n-1, a, c, b)
        move.append([a, c])
        hanoi(n-1, b, a, c)
        
move = [] # 이동 경로
hanoi(int(input()), 1, 2, 3)
print(len(move))
print('\n'.join([' '.join(str(i) for i in row) for row in move]))