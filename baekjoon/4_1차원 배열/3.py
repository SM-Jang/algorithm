# 3
"""
counter
"""
A = int(input())
B = int(input())
C = int(input())

counter = [0]*10
mul = A*B*C
while True:
    q, r = mul//10, mul%10
    if q == 0: 
        counter[r] += 1
        break
    
    mul = q
    counter[r] += 1

for cnt in counter:
    print(cnt)