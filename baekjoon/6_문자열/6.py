N = int(input())

def isGroup(string):
    n = len(string)
    for i in range(n-1):
        if string[i] == string[i+1]:
            continue
        elif string[i] in string[i+1:]:
            return False
    return True
        

cnt = 0
for _ in range(N):
    s = input()
    if isGroup(s):
        cnt+=1
        
print(cnt)