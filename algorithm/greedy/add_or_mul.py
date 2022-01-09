S = '02984'

result = 0
for i, s in enumerate(S):
    s = int(s)
    if result==0: # 처음 0일땐 무조건 더하기
        result+=s
        continue
    if s==0 or s==1: # 다음 숫자가 0 혹은 1이면 더하기가 더 커짐
        result += s
    else: # 2이상에서는 곱하기가 무조건 더 커짐
        result *= s
        
        
print(result)