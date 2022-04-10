import sys
# 1. 입력
n = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))

# 2. 정렬
y = sorted(set(X))

# 3. hash table
y_dict = {}
for i in range(len(y)):
    y_dict[y[i]] = i
    
# 4. 출력
for x in X:
    print(y_dict[x], end=' ')