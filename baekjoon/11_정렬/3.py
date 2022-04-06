# 시간제한: 5초, 공간제한: 8MB
import sys

# 빠른 입력
n = int(sys.stdin.readline().strip())

# 몇번 불렸는지 카운팅(0~10000까지)
numbers = [0] * (10001)
for _ in range(n):
    i = int(sys.stdin.readline())
    numbers[i] += 1
    

# 출력
for i in range(10001):
    if numbers[i] == 0: continue
    while numbers[i]:
        print(i)
        numbers[i]-=1