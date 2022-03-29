N = int(input())
candidates = map(int, input().split())

def isPrime(x):
    ans = True
    for i in range(2, x//2+1):
        if x%i == 0: 
            ans = False
            break
    return ans
            
    

cnt = 0
for candidate in candidates:
    if candidate == 1: continue
    if isPrime(candidate):
        cnt+=1
        
print(cnt)