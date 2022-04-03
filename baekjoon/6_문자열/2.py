T = int(input())
ans = []
for _ in range(T):
    R, S = input().split()
    R = int(R)
    
    result = ''
    for s in S:
        result += s*R
        
    ans.append(result)
    
for x in ans:
    print(x)