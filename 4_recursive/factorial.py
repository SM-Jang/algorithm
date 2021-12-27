def factorial(value:int) -> int:
    if value > 0:
        return value * factorial(value-1)
    else:
        return 1
    
if __name__ == '__main__':
    x = int(input('출력할 팩토리얼 값을 입력하세요:'))
    print(f'팩토리얼 결과 값은 {x}! = {factorial(x)}입니다.')
    
