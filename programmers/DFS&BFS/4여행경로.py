from collections import defaultdict
def solution(tickets):
    d = defaultdict(list)
    for t in tickets:
        d[t[0]].append(t[1])

    for k in d.keys():
        d[k].sort(reverse=True)

    print(d)
    stk = ['ICN']
    ans = []
    while stk:
        # print(stk)
        top = stk[-1]
        if d[top]:
            stk.append(d[top].pop())
        else:
            ans.append(stk.pop())

    return ans[::-1]