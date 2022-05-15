# gcd
def gcd(a,b):
    if a<b:
        a, b = b, a
    while b>0:
        a, b = b, a % b
    return a

# lcm
def lcm(a,b):
    return int(a*b/gcd(a,b))

## main
n1, n2 = map(int, input().split())
print(gcd(n1,n2))
print(lcm(n1,n2))
