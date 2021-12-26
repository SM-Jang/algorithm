from  typing import Any

class FixedStack:
    """고정된 길이의 스택"""
    
    class Empty(Exception):
        """비어 있는 고정스택에 팝 또는 피크할 때 내보내는 예외 처리"""
        pass
    
    class Full(Exception):
        """가득 찬 고정스택에 푸시할 떄 내보내는 예외 처리"""
        pass
    
    def __init__(self, capacity:int = 256) -> None:
        self.stack = [None] * capacity
        self.capacity = capacity
        self.ptr = 0
        
    def __len__(self) -> int:
        """스택에 쌓여 있는 데이터의 개수를 반환"""
        return self.ptr
    
    def is_empty(self) -> bool:
        """스택이 비어 있는지 판단"""
        return self.ptr<=0 # 비어 있을 때 True
    
    def is_full(self) -> bool:
        """스택이 가득 차 있는지 판단"""
        return self.ptr >= self.capacity
    
    def push(self, value: Any) -> None:
        if self.is_full():
            raise FixedStack.Full # 가득찬 예외 처리 
        else:
            self.stack[self.ptr] = value
            self.ptr +=1
            
    def pop(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty # 비어있는 예외 처리
        else:
            self.ptr -= 1
            return self.stack[self.ptr]
        
    def peek(self) -> Any:
        """스택의 데이터를 들여다봄"""
        if self.is_empty():
            raise FixedStack.Empty
        return self.stack[self.ptr-1]
        
    def clear(self) -> None:
        self.ptr=0
            
        
    def find(self, value:Any) -> Any:
        """스택에서 value를 찾아 인덱스를 반환(없으면 -1을 반환)"""
        
        for i in range(self.ptr-1, -1, -1): # 꼭대기에서 선형 검색
            if self.stack[i] == value: return i
            
        return -1
    
    def count(self, value:Any) -> bool:
        """스택에 있는 value의 개수를 반환"""
        c = 0
        for i in range(self.ptr): # 바닥부터 선형 검색
            if self.stack[i] ==value: c+=1
                
        return c
    
    def __contains__(self, value:Any) -> bool:
        """스택에 value가 있는지 없는지 확인"""
        return self.count(value) # 0이면 False, 이 외의 숫자면 True인 개념을 활용
    
    def dump(self) -> None:
        """덤프: 스택 안의 모든 데이터를 바닥부터 꼭대기 순으로 출력"""
        if self.is_empty():
            print('스택이 비어 있습니다.')
            
        else:
            print(self.stack[:self.ptr])
            
        