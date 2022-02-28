def isPrimeNumber(numParam1):
    """
    :param numParam1: 확인하는 숫자
    :return: prime->True
    """
    for itr in range(2, numParam1):
        if numParam1 % itr == 0:
            return False
    else:
        return True


def findPrimes(numParam1, numParma2):
    """
    :param numParam1: 시작 범위
    :param numParma2: 끝 범위
    :return: None, 해당 범위의 primes
    """
    numCount = 1
    for itr in range(numParam1, numParma2):
        if isPrimeNumber(itr):
            print(f'{numCount} th prime: {itr}')
            numCount += 1


findPrimes(1, 10)
