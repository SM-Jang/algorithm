from typing import MutableSequence

def partition(a: MutableSequence) ->None:
    n = len(a)
    pl = 0
    pr = n-1
    pivot = a[n//2]
    
    while pl <= pr:
        while a[pl] < pivot: pl+=1 # pivot보다 큰 index 찾기
        while a[pr] > pivot: pr-=1 # pivot보다 큰 index 찾기
        if pl<=pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
            
    print(f'피벗은 {pivot}입니다.')
    print(f'피벗 이하의 원소는 {a[:pl]}')
    print(f'피벗 이상의 원소는 {a[pr:]}')
    print('피벗과 일치하는 그룹')
    if pl > pr+1:
        print(a[pr+1:pl])
        
        
if __name__=='__main__':
    print('배열을 나눕니다')
    num = int(input('원소 수를 입력하시오:'))
    x = [None]*num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]='))
        
    partition(x)
    
        