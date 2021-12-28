from stack import Stack
from typing import MutableSequence

def qsort(a: MutableSequence, left:int, right:int) ->None:
    
    stk = Stack(right-left+1)
    stk.push((left, right))
    
    while not stk.is_empty():
        pl, pr = left, right = stk.pop()
        pivot = a[(left+right)//2]
        
        while pl <= pr:
            while a[pl] < pivot: pl+=1 # pivot보다 큰 index 찾기
            while a[pr] > pivot: pr-=1 # pivot보다 작은 index 찾기
            if pl<=pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1
        if left < pr: stk.push((left, pr))
        if pl < right: stk.push((pl, right))
    
    
    
    
    



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
    
        