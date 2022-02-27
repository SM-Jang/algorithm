def get(x):
    ans = []
    i=1
    while True:
        if x//i < i: break
        if x%i==0:
            ans.append((x//i, i))
        i+=1
    return ans

def solution(brown, yellow):
    ans = []
    for x, y in get(yellow):
        print(x,y, (x+y)*2+4)
        if (x+y)*2+4  == brown:
            ans = [x+2, y+2]
            break
    return ans