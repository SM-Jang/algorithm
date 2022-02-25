from collections import deque
def solution(prices):
    prices = deque(prices)
    ans = []
    while prices:
        cur = prices.popleft()
        cnt = 0
        for p in prices:
            cnt+=1
            if cur > p:break
        ans.append(cnt)

    return ans