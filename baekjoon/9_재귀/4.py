
answer=[]
def hanoi(n, a, b, c):
    if n==1:
        answer.append([a,c])
    else:
        # n-1 in a -> b
        hanoi(n-1, a, c, b)
        # n-th in a -> c
        answer.append([a, c])
        # n-1 in b -> 
        hanoi(n-1, b, a, c)
        
n = int(input())
hanoi(n, 1,2,3)
print(len(answer))
for ans in answer:
    print(ans[0], ans[1])