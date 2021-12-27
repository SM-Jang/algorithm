
def gcd(x:int, y:int) -> int:
    """유클리드 호제법"""
    if y ==0: return 0
    else: return gcd(y, x%y)
        
if __name__ == '__main__':
    print('두 정수의 최대 공약수를 구합니다.')
    
    x = int(input('정수 x를 입력하세요:'))
    y = int(input('정수 y를 입력하세요:'))
    
    print(f'gcd({x}, {y}) = {gcd(x,y)}')