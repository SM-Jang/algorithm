# main
n = int(input())
cost = []
for i in range(n):
    cost.append(list(map(int, input().split())))
    
# 다음 집값은 이전 집값 중 최소(자신을 빼고)
for i in range(1,n):
    cost[i][0] = min(cost[i-1][1], cost[i-1][2])+cost[i][0]# 빨강으로 칠했을 때, 최소 비용
    cost[i][1] = min(cost[i-1][0], cost[i-1][2])+cost[i][1]# 초록으로 칠했을 때, 최소 비용
    cost[i][2] = min(cost[i-1][0], cost[i-1][1])+cost[i][2]# 파랑으로 칠했을 때, 최소 비용
    
print(min(cost[n-1]))