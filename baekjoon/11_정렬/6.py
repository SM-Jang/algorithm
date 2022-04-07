import sys
# 1. 입력
n = int(sys.stdin.readline())
points = {}
for i in range(n):
    x,y = map(int, sys.stdin.readline().split(' '))
    
    # 2. hash자료형 활용
    if x in points:
        points[x].append(y)
    else:
        points[x] = [y]

# 3. key(x)를 기준으로 정렬
points = dict(sorted(points.items(), key=lambda x: x[0]))
for x, ys in points.items():
    # 4. value(y)를 기준으로 정렬
    ys.sort()
    for y in ys:
        # 5. 출력
        print(x, y)