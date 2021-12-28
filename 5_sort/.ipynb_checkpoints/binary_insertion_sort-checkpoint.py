
from typing import MutableSequence

def binary_insertion_sort(a: MutableSequence)->None:
    
    n = len(a)
    for i in range(1, n):
        key = a[i]
        start = 0
        end = i-1
        
        while True:
            center = (start+end)//2
            if a[center] == key: break
            elif a[center] < key: start = center+1
            else: end = center-1
            
            if start > end: break
            
        idx = center+1 if start <= end else end+1
        
        for j in range(i, idx, -1):
            a[j] = a[j-1]
        a[idx]= key
        print(a)
        
        
if __name__ == '__main__':
    print('이진 삽입 정렬')
    num = int(input('원소 수를 입력하세요:'))
    x = [None]*num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]='))
        
    binary_insertion_sort(x)
    print('오름차순으로 정렬')
    for i in range(num):
        print(x[i])