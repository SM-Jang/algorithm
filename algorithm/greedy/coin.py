
def exchange(money: int) -> dict:
    """
    :param money: 손님이 건낸 돈
    :return: 거스름돈 동전
    """
    # 거스름돈 동전의 개수에 대한 dictionary
    ans = {500 : 0,
           100 : 0,
           50  : 0,
           10  : 0}

    # 몫은 동전의 개수
    # 나머지는 남은 돈
    for coin in ans.keys():
        ans[coin] = money // coin
        money = money % coin

        if money == 0: break

    return ans



