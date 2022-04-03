# 1. 3점 입력
x, y = {}, {}
for _ in range(3):
    point = list(map(int, input().split()))

    # 2. counter
    if point[0] in x:
        x[point[0]] += 1
    else:
        x[point[0]] = 1

    if point[1] in y:
        y[point[1]] += 1
    else:
        y[point[1]] = 1
    
# 3. 1회 사용된 좌표 출력
for k, v in x.items():
    if v == 1: x = k

for k, v in y.items():
    if v == 1: y = k
    
print(x,y)

