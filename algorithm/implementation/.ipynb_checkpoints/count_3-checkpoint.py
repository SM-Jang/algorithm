# 시각
hour = int(input('시간:'))


count = 0
for h in range(hour+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h)+str(m)+str(s): count += 1
            
            
print(count)