
def hanoi(n, a,b,c):
    """
    n: 옮길 원판의 수
    a: 탑1(현위치 탑)
    b: 탑2
    c: 탑3(이동 될 탑)
    """
    # base condition
    global cnt
    cnt +=1
    if n==1:
        answer.append((a, c))
        return
    else:
        hanoi(n-1, a, c, b) # (n-1): a -> b
        answer.append((a, c)) # n-th: a -> c
        hanoi(n-1, b, a, c)


# main
n = int(input())
cnt = 0
answer=[]
hanoi(n, 1, 2, 3)
print(cnt)
for i in range(cnt):
    print(*answer[i])