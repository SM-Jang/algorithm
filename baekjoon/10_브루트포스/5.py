# https://claude-u.tistory.com/125
n = int(input())
movie = 666

while n: # 0일 될 때까지
    if '666' in str(movie): # 종말 수를 찾았을 때
        n -= 1 
    movie += 1 # 다음 종말수를 찾을 때까지 더해지기
print(movie -1)