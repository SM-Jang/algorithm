import sys
# 1. 입력
T = int(sys.stdin.readline())
# 2. DP 초기화
P = [-1]*101
P[0]=-1 # 없는 수
P[1]=1
P[2]=1
P[3]=1
P[4]=2
P[5]=2
# 3. 출력
for _ in range(T):
    n = int(sys.stdin.readline())
    
    if P[n] != -1:
        print(P[n])
    else:
        for i in range(6, n+1):
            # 점화식
            P[i]=P[i-1]+P[i-5]
        print(P[n])
    