from typing import Any

class FixedQueue:
    
    """Inter Exception Class"""
    class Empty(Exception):pass
    
    class Full(Exception): pass

    def __init__(self, capacity:int) -> None:
        self.capacity = capacity
        self.no = 0                    # 현재 큐에 들어있는 데이터의 수
        self.front = 0
        self.rear = 0
        self.que = [None] * capacity
        
    def __len__(self) -> int:
        return self.no
    
    def is_empty(self) -> bool:
        return self.no <= 0
    
    def is_full(self) -> bool:
        return self.no >= self.capacity
    
    def enque(self, x:Any) -> None:
        
        if self.is_full():
            raise FixedQueue.Full
            
        self.que[self.rear] = x
        self.rear = (self.rear+1) % self.capacity
        self.no += 1
        
    def deque(self) -> Any:
        
        if self.is_empty():
            raise FixedQueue.Empty
        
        out = self.que[self.front]
        self.front = (self.front+1)%self.capacity
        self.no -= 1
        return out
    
    
    def peek(self) -> Any:
        
        if self.is_empty():
            raise FixedQueue.Empty
            
        return self.que[self.front]
    
    def find(self, value:Any) -> Any:
        
        for i in range(self.no):
            idx = (i+self.front)%self.capacity
            if self.que[idx] == value:
                return idx
        return -1
    
    def count(self, value:Any) -> int:
        c = 0
        for i in range(self.no):
            idx = (i+self.front)%self.capacity
            if self.que[idx] == value: 
                c += 1
                
        return c
    
    def __contains__(self, value:Any) -> bool:
        return self.count(value)
    
    def clear(self) -> None:
        self.no=0
        self.front=0
        self.rear=0
        
    def dump(self) -> None:
        if self.is_empty():
            print('큐가 비어있습니다.')
        else:
            for i in range(self.no):
                idx = (i+self.front) % self.capacity
                print(self.que[idx], end='')
                
            print()
            
    
        
                