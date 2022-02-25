from collections import defaultdict
def solution(genres, plays):
    d = defaultdict(list)
    n = len(genres)
    for i in range(n):
        g, p = genres[i], plays[i]
        d[g].append(p)

    d2 = defaultdict(int)
    for k, v in d.items():
        d[k].sort(reverse=True)
        d2[k] += sum(v)
    d2 = sorted(d2.items(), key=lambda x: x[1], reverse=True)
    d2 = [x[0] for x in d2]

    ans = []
    for genre in d2:
        for play in d[genre][:2]:
            ans.append(plays.index(play))
    return ans