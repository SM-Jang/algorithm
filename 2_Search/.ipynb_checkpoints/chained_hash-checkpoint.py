from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    
    def __init__(self, key: Any, value:Any, next:None) -> None:
        self.key = key
        self.value = value
        self.next = next
        
        
class ChainedHash:
    """체인법으로 해시 클래스 구현"""
    def __init__(self, capacity: int) -> None:
        "초기화"
        self.capacity = capacity       # 해시 테이블의 크기
        self.table = [None]*capacity   # 해시 테이블 초기화
        
    def hash_value(self, key:Any) -> int:
        "해시값을 구하는 함수"
        if isinstance(key, int):
            return key % self.capacity
        else:
            return (int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)
        
    def search(self, key:Any) -> Any:
        """table에서 key를 찾아 원소를 검색하여 반환"""
        
        hash = self.hash_value(key)
        p = self.table[hash] # p is Node, 위에서 정의한 자료형태
        
        while p is not None:
            if p.key == key: return p.value
            p = p.next
        return None # 검색 실패
    
    def add(self, key: Any, value: Any) -> bool:
        """카가 key, 값이 value인 원소를 추가"""
        
        hash = self.hash_value(key)
        p = self.table[hash]
        
        while p is not None:
            # 같은 key를 갖는 노드가 있는지 검사
            if p.key == key: return False # 중복시 추가 실패
            p = p.next
            
        temp = Node(key, value, self.table[hash]) # 기존 노드를 가리키도록 지정
        self.table[hash] = temp # 해시 테이블은 새로운 노드를 가리키도록 지정
        return True
            
    def remove(self, key:Any) -> bool:
        """키가 key인 원소를 삭제"""
        
        hash = self.hash_value(key)
        p  = table[hash]
        pp = None
        
        while p is not None:
            # 현 노드가 맞을 때,
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True
            
            # 현 노드가 아닐 때,
            pp=p     # 이전 노드를 현 노드로
            p=p.next # 현 노드를 다음 노드로
            
        return -1 # key가 존재하지 않을 때, 삭제 실패
    
    
    def dump(self) -> None:
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f' -> {p.key}({p.value})', end='')
                p = p.next
                
            print()