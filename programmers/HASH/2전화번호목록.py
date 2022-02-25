def solution(phone_book):
    answer = True
    d={}
    # O(n)
    for x in phone_book:
        d[x] = d.get(x, 0) + 1

    #O(nm)
    for x in phone_book:
        temp = ''
        for number in x:
            temp+=number
            if temp in d and temp != x:
                answer = False
    return answer