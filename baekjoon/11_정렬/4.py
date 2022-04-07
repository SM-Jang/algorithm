import sys
# 1. 입력
n = int(sys.stdin.readline())


# 2. counter(dict로 구현)
counter = {}
for _ in range(n):
    idx = int(sys.stdin.readline())
    
    if idx in counter:
        counter[idx] += 1
    else:
        counter[idx] = 1
# key를 이용한 정렬
counter = dict(sorted(counter.items(), key= lambda x: x[0]))

# 3. 통계 구현
# 3-1. 산술평균
mean=0
for k, v in counter.items():
    mean += k*v
print(int(round(mean/float(n), ndigits=0)))

# 3-2. 중앙값
median=n//2+1
s=0
for k, v in counter.items():
    s+=v
    if median <= s:
        break
print(k)
# 3-3. 최빈값

mode = 0
# 최빈값을 찾고 
for k, v in counter.items():
    if mode < v: mode=v
# 최빈값에 해당하는 키값들 정리
modes = []
for k, v in counter.items():
    if v == mode: modes.append(k)

# 여러개일 경우 두 번째로 작은 값 출력
if len(modes)==1: print(modes[0])
else: print(modes[1])

    # 3-4. 범위
m, M = list(counter.keys())[0], list(counter.keys())[-1]
print(M-m)