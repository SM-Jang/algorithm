from typing import Any, Sequence
import numpy as np

    
    
def max_of(a: Sequence) -> Any:
    """시퀀스 a를 받아 최댓값을 반환"""
    maximum = a[0]
    
    for i in a:
        if maximum<i:
            maximum = i
            
    return maximum


if __name__ == '__main__':
    print(f"{np.__name__}")
    asd = temp()
    print(asd.__name__)
    print('배열의 최댓값을 구합니다.')
    num = int(input('원소 수를 입력하시오. '))
    
    x = [None] * num # init
    
    for i in range(num):
        x[i]=int(input(f'x[{i}]값을 입력하세요.:'))
        
        
    print(f'최댓값은{max_of(x)}')