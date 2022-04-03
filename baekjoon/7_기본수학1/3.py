n=int(input())
def solution(n):
    if n == 1: 
        return 1
    else:
        k=1
        while True:
            n1, n2 = 1+k*(k+1)/2, (k+1)*(k+2)/2
            
            if n1<=n and n<=n2:
                break
            else:k+=1
        return k+1, n1
if n == 1: print('1/1')
else:

    
    # 층 찾기
    floor, start = solution(n)
    # print(floor, start)
    # 층에 해당하는 리스트
    lst = [f'{x}/{floor+1-x}' for x in range(1, floor+1)]
    if floor % 2 != 0:
        lst = lst[::-1]
    print(lst[n-int(start)])
