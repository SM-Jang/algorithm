## main
n = int(input())
a = list(map(int, input().split()))

dp = [0]*n # 자신을 포함하여 만들 수 있는 부분 수열의 크기
for i in range(n): # 현 위치
    for j in range(i):
        if a[i]>a[j] and dp[i]<dp[j]:
            dp[i] = dp[j]
    dp[i]+=1
print(max(dp))