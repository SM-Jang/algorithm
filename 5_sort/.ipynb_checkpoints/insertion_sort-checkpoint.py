from typing import MutableSequence

def insertion_sort(a:MutableSequence) -> None:
    n = len(a)
    for i in range(1, n):
        j=i
        tmp = a[i]
        while j > 0 and a[j-1]>tmp: 
            # 큰 원소들을 오른쪽으로 밀어내느 작업
            a[j] = a[j-1]
            j -= 1
            
        a[j]= tmp
        
if __name__ == '__main__':
    print('단순 삽입 정렬')
    num = int(input('원소 수를 입력하세요:'))
    x = [None]*num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]='))
        
    insertion_sort(x)
    print('오름차순으로 정렬')
    for i in range(num):
        print(x[i])