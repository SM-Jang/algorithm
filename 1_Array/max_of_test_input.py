from max import max_of

print('배열의 최댓값을 구합니다.')
print('주의: "END"를 입력하면 종료합니다.')


number = 0

x = []

while True:
    print('list 초기화')
    s = input(f'x[{number}] 값을 입력하시오')
    if s=='END': break
        
    x.append(int(s))
    number +=1
    
print(f'{number}개를 입력하였습니다.')
print(f'최댓값은 {max_of(x)}')

    
    