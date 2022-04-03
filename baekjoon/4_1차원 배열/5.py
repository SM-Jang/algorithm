# 5
n = int(input())
scores = list(map(int, input().split(' ')))

# 최댓값 M
M = 0 
for score in scores:
    if score > M: M = score

# else: x/M*100
total = 0
for score in scores:
    total += score/M*100
    
print(total/n)    