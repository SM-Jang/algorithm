# 입력
N = int(input())

def isPrime(x):
    if x in [0,1]: return False
    ans=True
    for i in range(2,x//2+1):
        if x % i == 0: 
            ans=False
            break
    return ans

# 자체소수o
if isPrime(N):
    print(N)
# 자체소수x
else:
    # 소인수 찾기
    candidates = []
    for i in range(1,N):
        if N % i == 0 and isPrime(i):
            candidates.append(i)
            
    # 출력
    for candidate in candidates:
        while N % candidate==0:
            print(candidate)
            N = N // candidate
        