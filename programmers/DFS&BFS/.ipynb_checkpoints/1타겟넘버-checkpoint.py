def solution(numbers, target):
    sup = [0]
    while numbers:
        n = numbers.pop(0)
        sub = []
        for s in sup:
            sub.append(s+n)
            sub.append(s-n)
        sup = sub

    return sup.count(target)