# 상하좌우

n = int(input('지도의크기:'))
plans = input('계획서:').split(' ')

# 시작 위치
x, y = 1, 1

# L, R, U, D
dx = [0, 0, -1, +1]
dy = [-1, +1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            # 현위치에서 plan에 따라 찍힐 좌표
            x_ = x+dx[i] 
            y_ = y+dy[i]

    # 지도를 벗어나는 경우 채크
    if x_>n or x_<1 or y_>n or y_<1: continue
    x,y = x_, y_
    # print(x, y)
print(x, y)