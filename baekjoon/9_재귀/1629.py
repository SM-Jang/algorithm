
def func(a,b,c):
    if b==1: return a%c
    
    var = func(a, b//2, c)
    ans = (var * var)%c
    if b%2 == 0: return ans
    else:
        return (ans*a)%c


# main
a, b, c = map(int, input().split())
print(func(a,b,c))