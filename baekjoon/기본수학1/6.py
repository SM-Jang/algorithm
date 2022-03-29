T = int(input())

# 층(row), 호(col)
ks,ns = [],[]
for _ in range(T):
    ks.append(int(input()))
    ns.append(int(input()))
    
    
for i in range(T):
    k,n = ks[i], ns[i]
    
    # 아파트 생성
    apartment = []
    for floor in range(k+1):
        apartment.append([-1]*n)
    # (0층 ~ k-1층)까지 초기화
    for floor in range(k):
        for room in range(n):

            # 0층 초기화
            if floor == 0:
                apartment[floor][room]=room+1

            # 1층 부터 k-1층까지 bottom-up으로 정의
            else:
                apartment[floor][room] = sum(apartment[floor-1][:room+1])

    # (k층, n호), 주의: 호는 0호를 1호로 간주
    apartment[k][n-1] = sum(apartment[k-1][:n-1+1])
    print(apartment[k][n-1])