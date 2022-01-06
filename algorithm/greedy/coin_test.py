import time

from coin import exchange
import time

if __name__ == '__main__':
    while True:
        money = int(input('받은 돈은:'))

        # 1의 자리 숫자는 받지 않는다
        if money % 10 == 0: break

    start = time.time()
    coins = exchange(money)
    end = time.time()
    count = 0
    print(f'알고리즘 소요 시간: {start - end}')
    for k, v in coins.items():
        print(f'동전 {k}: {v}개')
        count += v

    print(f'총 {count}개의 동전 사용')
