def fibo(n):
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        

n = int(input())
dp = [1] * 41
fibo(40)
for _ in range(n):
    
    x = int(input())
    if x==0:
        print('1 0')
    elif x==1:
        print('0 1')
    else:
        print(f'{dp[x-2]} {dp[x-1]}')
    
    
    