# 7
C = int(input())
ans = []
for i in range(C):
    case = list(map(int, input().split(' ')))
    
    n, scores = case[0], case[1:]
    mean = sum(scores)/n
    cnt = 0
    
    for score in scores:
        if score > mean: 
            cnt+=1
    x = cnt/n*100
    ans.append(x)
for a in ans:
    print("{:2.3f}".format(a))
        