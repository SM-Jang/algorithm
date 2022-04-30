def make_seq(depth, m):
    # 종료
    if depth >= m:
        print(*output)
        return
    
    # depth에 값 넣기
    for x in arr:
        if x in output: continue
        output[depth] = x
        make_seq(depth+1, m)
        output[depth] = 0
        
    
    
    
# main
n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
output = [0]*m

make_seq(0, m)