from math import sqrt
n = int(input())

for _ in range(n):
    # 0. 반복 입력
    x1,y1,r1, x2,y2,r2 = map(int, input().split())
    
    # 1. 수치값 계산
    dist = sqrt( (x1-x2)**2 + (y1-y2)**2 )
    rSum = r1+r2
    rMinus = abs(r1-r2)
    
    # case1. 중심점이 같을 때
    if dist == 0:
        if r1==r2: print(-1)
        else: print(0)
    # case2. 중심점이 다를 떄
    else:
        if dist == rSum or dist==rMinus:
            # 외접 혹은 내접
            print(1)
        elif dist < rSum and dist > rMinus:
            # 외접 혹은 내접
            print(2)
        else:
            print(0)
    