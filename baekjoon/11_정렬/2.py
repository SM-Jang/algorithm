# 시간제한 2 초, 공간제한 256 MB
import sys

# 빠른 입력
n = int(sys.stdin.readline().strip())

# 공간 제한 할당(공간 복잡도 O(n)), array형 자료구조 이용
numbers = [-1] * (n)

# 할당 O(1)
for i in range(n):
    numbers[i] = int(sys.stdin.readline())
    
# 정렬 O(nlog(n))
numbers.sort()

# 출력 O(n)
for number in numbers:
    print(number)