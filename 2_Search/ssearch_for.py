from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 같은 원소를 선형 검색"""

    for i, value in enumerate(a):
        if value == key: return i
    else: return -1
        
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