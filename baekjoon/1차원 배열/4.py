# 4
d = {}
for i in range(10):
    x = int(input())
    d[x%42] = 1
    
print(len(d))