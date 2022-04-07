import sys
# 1. 입력
n = int(sys.stdin.readline())

# 2. 각 자리는 0~9이니까 counter이용
counter = [0]*10
while n:
    q, r = n//10, n%10
    counter[r]+=1
    n = q
    
# 3. key*count
ans = ''
for i in range(9, -1, -1):
    ans+=str(i)*counter[i]
    
# 출력
print(ans)