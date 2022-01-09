# 왕실의 나이트
p = input()
# input_data = input()
# row = int(input_data[1])
# col = int(ord(input_data[0])) - int(ord('a')) +1 
row = ['1','2','3','4','5','6','7','8']
col = ['a','b','c','d','e','f','g','h']

cases = ((+2,+1), (+2,-1), (-2,+1), (-2,+1),
       (+1,+2),(+1,-2),(-1,+2),(-1,-2),)

# 위치 찾기
for i in p:
    if i in row:
        r = row.index(i)
    if i in col:
        c = col.index(i)

count=0
for case in cases:
    dx,dy = case[0], case[1]
    if 1<=(r+dx) and (r+dx)<=8 and 1<=(c+dy) and (c+dy)<=8:
        count+=1
        
print(count)
    