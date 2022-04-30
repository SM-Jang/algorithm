def f(n, r, c):
    if n==0: return 0
    # import pdb; pdb.set_trace()
    # 몇사분면에 속하는지 확인
    x = 2**n
    x = x//2
    if (r<x) and (c<x): #1
        value = 4**(n-1)*0
    elif (r<x) and (c>=x): #2
        value = 4**(n-1)*1
    elif (r>=x) and (c<x): #3
        value = 4**(n-1)*2
    else: #4
        value = 4**(n-1)*3
        
    ans = value+f(n-1,r%x,c%x)
    return ans


# main
n,r,c = map(int, input().split())
print(f(n,r,c))