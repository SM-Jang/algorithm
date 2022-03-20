S = 'baekjoon'
pos = [-1]*(ord('z')-ord('a')+1)

for i in range(len(S)):
    index = ord(S[i]) - ord('a')
    if pos[index]==-1:
        pos[index]=i
    else:
        if pos[index] > i:
            pos = i

for i in pos:
    print(i, end=' ')