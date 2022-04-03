# 시간:O(n), 공간:O(n)
n = int(input())
# 1. DP table 초기화
fibo = [0]*21
fibo[0] = 0
fibo[1] = 1
if n < 2:
    print(fibo[n])
else: # 2. Bottom-up으로 계산
    for i in range(2,n+1):
        fibo[i]=fibo[i-1]+fibo[i-2]
        
    print(fibo[n])