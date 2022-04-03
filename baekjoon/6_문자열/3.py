s = input()
s = s.upper()
s_list = list(set(s))

cnt = []
for x in s_list:
    cnt.append(s.count(x))
    
if cnt.count(max(cnt))>1:
    print("?")
else:
    print(s_list[cnt.index(max(cnt))])
    