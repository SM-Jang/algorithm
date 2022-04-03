from bisect import bisect_left, bisect_right
from math import sqrt

# 소수 판별 함수(효율화)
def isPrime(x):
    if x == 1: return False
    ans = True
    for i in range(2, int(sqrt(x))+1):
        if x%i==0:
            return False
    return ans


# 소수 기록(DP)
Prime = []
for i in range(2, 246912):
    if isPrime(i):
        Prime.append(i)
        
while True:
    # 입력
    n = int(input())
    if n==0: break

    # n보다 크고 2n보다 작거나 같은 소수의 개수 카운트
    cnt = bisect_right(Prime, 2*n) - bisect_left(Prime, n+1)
    
    # 출력
    print(cnt)
