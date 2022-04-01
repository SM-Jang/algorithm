from math import pi

# 1. 반지름 입력(r) -> 원의 넓이(pi*r^2)
r = int(input())
area1 = pi*(r**2)
print(f'{area1:.6f}')
# 2. 사각형의 넓이 구하기(2r^2)
area2 = 2*(r**2)
print(f'{area2:.6f}')
