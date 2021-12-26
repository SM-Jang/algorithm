해당 코드는 'Do-it 자료구조와 함께 배우는 알고리즘 입문 - 파이썬편'을 공부한 내용입니다.

각 단원별로 중요하다고 여기는 부분을 작성한 파일입니다

자료구조: 데이터 단위와 데이터 자체 사이의 물리저또는 논리적인 관계
          즉, 자료구조는 데이ㅣ터가 모여 있는 구조 
          + 컴퓨터에서 처리해야하는많은 데이터를 모아 효율적으로 관리하고 구조화
          
          
annotations 주석과 같음, 그냥 자료형을 명시해주는 표현

1_Array

저장된 데이터에서 원하는 자료를 찾는 방법:
 - 최댓값 찾기: max
 - 반복문 사용: for, while (+ enumerate)
데이터 형태
 - 뮤터블: 리스트(list), 딕셔너리(dict), 집합(set) - 변경가능
 - 이뮤터블: 수(number - int,float .etc), 문자열(String), 튜플(tuple) - 변경불가능
 linear search
 (number2)//(number1): 1로 2를 나눈 몫
 (number2)%(number1): 1로 2를 나눈 나머지
 
 y = x.copy()
 shallow copy : 리스트 x가 참조하는 곳이 다르면 y도 달라진다 (참조 복사)
 
 import coy
 y = copy.deepcopy(x)
 deep copy: 참조값 뿐만 아니라 참조하는 객체 자체를 복사 (전체 복사)
 
2_Search

keyword: key, value, sorted_data, complelxity
idea: 반복을 통해 값을 찾음
      반복문 자체가 적거나 반복문을 끝내는 조건문이 적을 수록 효과적
- 선형 검색(linear search): 무작위로 늘어놓은 데이터 집합에서 검색을 수행 O(n)
- 이진 검색(binary search): 일정한 규칙으로 늘어놓은 데이터 집합에서 아주 빠른 검색을 수행 O(log(n))
- 해시법: 추가, 삭제가 자주 일어나는 데이터 집합에서 아주 빠른 검색을 수행
    체인법: 같은 헤시값 데이터를 연결 리스트로 연결하는 방법
    오픈 주소법: 데이터를 위한 해시값이 충돌할 떄 재해시하는 방법
 
 3_stack&queue
 
 데이터를 임시로 저장하는 자료구조
 
 stack - LIFO(Last In Frist Out)
 push, pop, top, bottom, capacity, ptr
 list형 