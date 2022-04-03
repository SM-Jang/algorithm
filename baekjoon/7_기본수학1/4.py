a, b, v = map(int, input().split())

dist = a-b
q, r = (v-a)//dist, (v-a)%dist
if r==0: print(q+1)
else: print(q+2)