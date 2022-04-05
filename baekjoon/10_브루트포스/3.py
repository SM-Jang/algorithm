# 1. 입력 -> 덩치 table
n = int(input())
people = []
for _ in range(n):
    weight, height = map(int, input().split())
    people.append((weight, height))

# 2. 1명씩 비교 -> cnt
answer = [1]*n
for i in range(n):
    cnt = 0
    for j in range(n):
        if i == j: continue
        # 무게, 키 모두 크면 덩치 등수에 반영
        if (people[i][0]<people[j][0]) and people[i][1]<people[j][1]: cnt+=1
        
    answer[i]=cnt+1
    
# 3. 출력
for ans in answer:
    print(ans, end=' ')