import sys
# 1. 입력
n = int(sys.stdin.readline())

points = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x,y))


# 2. y기준 정렬 O(nlog(n))
points = sorted(points, key=lambda x: x[1])

# 3. hash table(dict)- key:y, value:x O(n)
table = {}
for x,y in points:
    if y in table:
        table[y].append(x)
    else:
        table[y] = [x]
        
# 4. 순서대로 출력 O(n)
for y,xs in table.items():
    for x in sorted(xs):
        print(x, y)