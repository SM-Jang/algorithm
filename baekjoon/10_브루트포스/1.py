n, m = map(int, input().split())
card = list(map(int, input().split()))



def blackJack(card):
    answer = 0
    # 완전 탐색
    for c1 in range(n):
        for c2 in range(c1+1, n):
            for c3 in range(c2+1,n):
                s = card[c1]+card[c2]+card[c3]
                if s<=m: 
                    answer = max(answer, s)
    return answer
            
answer = blackJack(card)
print(answer)