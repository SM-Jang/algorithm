# 입력
n = int(input())

def f(x):
    # 1의 자리
    if x<10: return 2*x
    ans = x
    while x>=10:
        q, r = x//10, x%10
        ans += r
        x=q
    ans+=q
    return ans

answer = 0
# 1. n까지 반복
for i in range(1, n):
    # 2. 분해합
    if f(i)  == n:
        answer=i
        break
# 출력 
print(answer)