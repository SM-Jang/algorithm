from typing import Any, Sequence
import copy

def seq_search(seq: Sequence, key: Any) -> int:
    """ 시퀀스 seq에서 key와 일치하는 원소를 선형 검색(보초법)"""
    
    a = copy.deepcopy(seq)
    a.append(key)
    
    for i, value in enumerate(a):
#         print(i, value, key)
        if value == key: break
    
    return -1 if (i+1) == len(a) else i

if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요:'))
    x = [None]*num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]='))
        
    key = int(input('검색할 key를 입력하세요:'))
    
    idx = seq_search(x, key)
    
    if idx==-1:
        print('검색값을 갖는 원소는 없습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')