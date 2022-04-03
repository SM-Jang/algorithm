n = int(input())

def solution(n):
    k = 1
    while True:
        n1, n2 = 2 + 6*k*(k-1)/2, 1 + 6*k*(k+1)/2
        # print(n1, n , n2)
        if n1<=n and n<=n2:
            break
        else:k+=1
    return k

if n == 1: print(1)
else:
    k = solution(n)
    print(k+1)
    