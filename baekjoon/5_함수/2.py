N = 10000

def d(n):
    ans = n
    while n > 0:
        ans += (n % 10)
        n = (n // 10)
    return ans

table = [False] * (N+1)
for n in range(1, N+1):
    index = d(n)
    if index < N+1:
        table[index]= True

for i in range(1, N):
    if table[i]==False:
        print(i)