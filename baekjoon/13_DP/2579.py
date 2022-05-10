## main
n = int(input())
s = [0 for i in range(301)]
dp = [0 for i in range(301)]
for i in range(n):
    s[i] = int(input())
    
## dp
dp[0]=s[0] # 1
dp[1]=s[0]+s[1] # 2
dp[2]=max(s[0]+s[2],s[1]+s[2]) # 3
for i in range(3,n):
    # 현계단 + 전계단 vs 현계단 + 전전계단
    dp[i] = s[i] + max(s[i-1]+dp[i-3], dp[i-2])
print(dp[n-1])