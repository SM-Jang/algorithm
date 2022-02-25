def solution(clothes):
    d = {}
    for n, t in clothes:
        d[t] = d.get(t,0)+1

    ans = 1
    for v in d.values():

        ans *= (v+1)
    return ans-1