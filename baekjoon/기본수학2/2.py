M = int(input())
N = int(input())

def isPrime(x):
    if x in [0, 1]: return False
    ans = True
    for i in range(2, x//2+1):
        if x%i == 0: 
            ans = False
            break
    return ans

prime = []
for i in range(M, N+1):
    if isPrime(i):
        prime.append(i)
        
if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(prime[0])