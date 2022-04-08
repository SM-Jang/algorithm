import sys
# 1. 입력
n = int(sys.stdin.readline())

# 문자열 배열
words = []
for i in range(n):
    word = sys.stdin.readline().strip()
    words.append((len(word), word))
    
    
# 2. 길이순 정렬
words = sorted(words, key=lambda x: x[0])

# 3. 헤시 테이블 key: length, value: [word]
table = {}
for length, word in words:
    if length in table:
        if word not in table[length]: # 중복 제거
            table[length].append(word)
    else:
        table[length] = [word]
        
# 4. value 사전순 정렬 출력
for k, v in table.items():
    for w in sorted(v): 
        print(w)