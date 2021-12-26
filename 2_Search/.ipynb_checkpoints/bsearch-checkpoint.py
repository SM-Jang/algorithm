from typing import Sequence, Any

def bin_search(seq: Sequence, key: Any) -> int:
    """시퀀스 seq에서 값 key를 이진 검색으로 찾아 인덱스를 리턴"""
    
    # 시작 끝 인덱스
    start = 0
    end = len(seq)-1
    
    while start < end:
        center = (start + end) // 2 # 중간 인덱스
        
        if seq[center] == key: return center
        if seq[center] < key: end=center-1
        if seq[center] > key: start=center+1
            
        
    
    return -1

if __name__ == '__main__':
    # init
    num = int(input('원소 수를 입력:'))
    x = [None]*num
    
    # sequence
    print('오름 차순으로 배열을 입력')
    x[0] = int(input('x[0]:'))
    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]:'))
            if x[i] >= x[i-1]: break
                
    key = int(input('검색할 값을 입력하시오:'))
    
    idx = bin_search(x, key)
    
    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 존재')
        