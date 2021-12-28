from typing import MutableSequence

def selection_sort(a:MutableSequence) -> None:
    """단순 선택 정려"""
    n = len(a)
    for i in range(n-1):
        m = i
        
        for j in range(i+1, n):
            if a[j] < a[m]: m = j
            
        a[i], a[m] = a[m], a[i]