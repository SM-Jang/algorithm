def han(x):
    r = []
    d = (x % 10) - ((x % 100) // 10)
    
    while x > 0:
        r.append(x%10)
        x = x//10
    
    for r1, r2 in zip(r[:-1], r[1:]):
        if r1 - r2 != d: return False
    
    return True

N = int(input())
cnt = 0
for i in range(1, N+1):
    
    if han(i): cnt += 1
    
print(cnt)