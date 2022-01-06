from enum import Enum
from fixed_queue import FixedQueue

Menu = Enum('메뉴', ['인큐','디큐','피크','검색','덤프','종료'])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep=' ', end='')
        n = int(input(': '))
        if 1 <= n <= len(s): return Menu(n)
    
q = FixedQueue(64)

while True:
    print(f'현재 데이터 개수:{len(q)}/{q.capacity}')
    menu = select_menu()
    
    if menu == Menu.인큐:
        x = int(input('인큐할 데이터를 입력하시오:'))
        try:
            q.enque(x)
        except FixedQueue.Full:
            print('큐가 가득 찼습니다.')
            
    elif menu == Menu.디큐:
        try:
            out = q.deque()
            print(f'디큐한 데이터는 {out}입니다.')
        except FixedQueue.Empty:
            print('큐가 비어있습니다.')
            
    elif menu == Menu.피크:
        try:
            r = q.peek()
            print(f'피크한 데이터는 {r}입니다.')
        except FixedQueue.Empty:
            print('큐가 비어있습니다.')
            
    elif menu == Menu.검색:
        key = int(input('검색할 데이터를 입력하세요:'))
        if key in q: # __contains__
            count = q.count(key)
            idx = q.find(key)
            print(f'{key}는 {count}개 포함되어 있고 {idx} 위치에 최초로 있습니다.')
            
        else: print(f'{key}는 큐에서 찾을 수 없습니다.')
        
    elif menu == Menu.덤프:
        q.dump()
        
    else: break