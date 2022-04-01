import heapq
from math import sqrt

# 내 풀이

# 0. 입력
T = int(input())

# 1. 소수 메모
def isPrime(x):
    if x==1: return False
    else:
        for i in range(2, int(sqrt(x)+1)):
            if x%i == 0: return False
    return True
prime = []
for i in range(10000):
    if isPrime(i):
        prime.append(i)


for _ in range(T):
    n = int(input())
    q = [] # 우선순위 큐
    
    # 2. n에 대한 골드바흐 파티션 구히가
    for p1 in prime:
        if p1 < n: # 2-1. n보다 작은 소수 중에서
            p2 = n-p1
            if p2 < p1: break # 중복 제거
            if isPrime(p2): # 2-2. p2(=n-p1)도 소수이면
                heapq.heappush(q, (abs(p1-p2), (p1, p2))) # (차이, (p1, p2))
    ans = heapq.heappop(q)
    print(f'{ans[1][0]} {ans[1][1]}')

