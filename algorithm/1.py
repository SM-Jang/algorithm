def func1(n):
    ans = []
    for i in range(1, n):
        if (i%3==0) | (i%5==0):
            ans.append(i)
    return sum(ans)
func1(16)

