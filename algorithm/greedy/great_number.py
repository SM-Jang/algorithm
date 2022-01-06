import time


def solution(data, M, K) -> int:

    answer = 0
    data.sort()
    print(data)

    count=0 # 사용 횟수
    for _ in range(M):
        if count==K:
            answer+=data[-2] # 다음으로 큰 수
            count=0 # 초기화
        else:
            answer+=data[-1] # 가장 큰수
            count+=1

    return answer



if __name__=='__main__':
    N, M, K = map(int, input('N, M, K를 띄어쓰기로 입력하시오:').split())

    data = []
    for _ in range(N):
        data.append(int(input('데이터를 입력하시오:')))

    start=time.time()
    great = solution(data, M, K)
    end=time.time()
    print(f'Spent time: {end-start}')
    print(f'Greatest Number is {great}')
