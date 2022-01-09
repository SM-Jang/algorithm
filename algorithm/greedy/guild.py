n = int(input())
data = list(map(int, input().split(' ')))
data.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data:
    count += 1 # 그룹에 포함
    if count >= i: # 모험가의 수 >= 공포도
        result += 1 # 그룹 수 증가
        count = 0
        
print(result)
    