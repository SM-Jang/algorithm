# 2
arr = []
M = 0
idx = 0
for i in range(9):
    x = int(input())
    if x>M: 
        M = x
        idx = i
        
print(M)
print(idx+1)
