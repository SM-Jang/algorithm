import sys

# 1. 입력
n = int(sys.stdin.readline())

members = []
for _ in range(n):
    # age, name
    member = list(sys.stdin.readline().split())
    members.append(member)
    
# 2. 나이순 정렬
members = sorted(members, key=lambda x: int(x[0]))

# 3. 출력
for i in range(n):
    print(members[i][0], members[i][1])