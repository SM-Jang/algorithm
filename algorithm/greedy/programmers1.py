def solution(n, lost, reserve):
    # 갖고있는 학생
    answer = n - len(lost)
    # lost.sort()
    # reserve.sort()
    
    inter = set(lost)&set(reserve)
    answer += len(inter)
    lost = list(set(lost)-inter)
    reserve = list(set(reserve)-inter)
            
    for l in lost:
        if len(reserve)==0: break
        if (l-1) in reserve: 
            answer+=1
            reserve.remove(l-1)
            continue
            
        elif (l+1) in reserve:    
            answer+=1
            reserve.remove(l+1)
            continue

    return answer