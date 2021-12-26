from __future__ import annotations
from typing import Any, Type
from enum import Enum
import hashlib

# 버킷속성
class Status(Enum):
    # Enum을 상속하여 만든 데이터 타입
    OCCUPIED = 0 # 데이터 저장
    EMPTY = 1 # 비어있는 상태
    DELETED = 2 # 삭제된 상태

    
class Bucket:
    """해시를 구성하는 버킷"""
    
    def __init__(self, key:Any = None, value:Any = None,
                stat:Status = Status.EMPTY):
        self.key = key
        self.value = value
        self.stat = stat
        
    def set(self, key:Any, value:Any, stat:Status) -> None:
        self.key=key
        self.value=value
        self.stat=stat
        
    def set_status(self, stat:Status)->None:
        self.stat=stat
        
class OpenHash:
    """오픈 주소법으로 해시 클래스 구현"""
    def __init__(self, capacity: int) -> None:
        "초기화"
        self.capacity = capacity       # 해시 테이블의 크기
        self.table = [Bucket()]*capacity   # 해시 테이블 초기화
        
    def hash_value(self, key:Any) -> int:
        "해시값을 구하는 함수"
        if isinstance(key, int):
            return key % self.capacity
        else:
            return (int(hashlib.md5(str(key).encode()).hexdigest(), 16) % self.capacity)
        
        
    def rehash_value(self, key:Any) -> int:
        return (self.hash_value(key)+1) % self.capacity
        
        
    def search_node(self, key:Any) -> Any:
        """키가 key를 찾아 위치 반환"""
        
        hash = self.hash_value(key)
        p = self.table[hash] # p is Node, 위에서 정의한 자료형태
        
        for i in range(self.capacity):
            if p.stat == Status.EMPTY: break
            elif p.stat == Status.OCCUPIED and p.key == key:
                return p
            hash = self.rehash_value(hash)
            p=self.table[hash]
        return None
    
    def search(self, key:Any) -> Any:
        """table에서 key를 찾아 원소를 검색하여 반환"""
        
        p = self.search_node(key)
        if p is not None: return p.value
        else: return None

    
    def add(self, key: Any, value: Any) -> bool:
        """키가 key, 값이 value인 원소를 추가"""
        if self.search(key) is not None:
            return False # 이미 등록된 키
        
        hash = self.hash_value(key)
        p = self.table[hash]
        
        for i in range(self.capacity):
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True
            
            hash = self.rehash_value(hash)
            p = self.table[hash]
        return False # 해시 테이블이 가득 참
    
    
    def remove(self, key:Any) -> bool:
        """키가 key인 원소를 삭제"""
        
        p  = self.search_node(key)
        if p is None: return False
        p.set_status(Status.DELETED)
        return True

    
    
    def dump(self) -> None:
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f' -> {p.key}({p.value})', end='')
                p = p.next
                
            print()