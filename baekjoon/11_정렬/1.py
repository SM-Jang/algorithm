# 시간제한1 초, 공간제한 128 MB

n = int(input())
# 자료형(array)
numbers = [] 
for _ in range(n):
    # 시간 복잡도 array의 삽입(O(1)) * n -> O(n)
    numbers.append(int(input()))
    
for number in  sorted(numbers): # 정렬: O(nlog(n)), 반복 O(n)
    print(number)
    
# 시간복잡도: O(nlog(n)), 공간복잡도: O(n)
