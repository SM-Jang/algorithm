from typing import MutableSequence

def qsort(a: MutableSequence, left:int, right:int) ->None:
    n = len(a)
    pl = left
    pr = right
    pivot = a[(left+right)//2]
    
    print(f'a[{left}] ~ a[{right}]:', *a[left:right+1])
    
    
    while pl <= pr:
        while a[pl] < pivot: pl+=1 # pivot보다 큰 index 찾기
        while a[pr] > pivot: pr-=1 # pivot보다 큰 index 찾기
        if pl<=pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
    if left < pr: qsort(a, left, pr)
    if pl < right: qsort(a, pl, right)

def quick_sort(a: MutableSequence) -> None:
    qsort(a, 0, len(a)-1)
        
if __name__=='__main__':
    print('퀵 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하시오:'))
    x = [None]*num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]='))
        
    quick_sort(x)
    
    print('오름차순으로 정렬')
    for i in range(num):
        print(f'x[{i}]={x[i]}')
    
        