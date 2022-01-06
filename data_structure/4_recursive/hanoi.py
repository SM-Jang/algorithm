def  move(no: int, x: int, y: int) -> None:
    """원반 no개를 x기둥에서 y기둥으로 옮김"""
    if no > 1:
        move(no - 1, x, 6-x-y)
        
    print(f'원반 [{no}]를 {x} -> {y}로 옮김')
    
    if no > 1:
        move(no -1, 6-x-y, y)
        
if __name__ == '__main__':
    print('하노이의 탑을 구현')
    n = int(input('원반의 개수를 입력하세요:'))
    move(n, 1, 3)