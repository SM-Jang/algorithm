def card_conv(x:int, y:int) -> str:
    """정수 x 를 r진수로 변환한 뒤 그 수를 나타내는 문자열을 반환"""
    
    d = ''
    dchar ='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while x>0:
        d += dchar[x%y] 
        x //= y
    
    return d[::-1]

if __name__ == "__main__":
    print('10진수를 n진수로 변환합니다.')
    
    while True:
        while True:
            no = int(input('변환할 값으로 음이 아닌 정수를 입력하세요.:'))
            if no > 0 : break
                
        while True:
            cd = int(input('어떤 진수로 변화할까요?:'))
            if 2 <= cd and cd <=36: break
                
        print(f'{cd}진수로는 {card_conv(no, cd)}')
        
        retry = input("한 번 더 변환할까요?(y or n)")
        if retry in {'N', 'n'}: break
            
                