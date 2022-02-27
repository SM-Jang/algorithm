def solution(answers):
    n = len(answers)

    seq1 = [1,2,3,4,5]
    seq2 = [2,1,2,3,2,4,2,5]
    seq3 = [3,3,1,1,2,2,4,4,5,5]

    n1 = len(seq1)
    n2 = len(seq2)
    n3 = len(seq3)

    a1, a2, a3 = n//n1, n//n2, n//n3
    b1, b2, b3 = n%n1, n%n2, n%n3

    ans1 = seq1*a1 + seq1[:b1]
    ans2 = seq2*a2 + seq2[:b2]
    ans3 = seq3*a3 + seq3[:b3]

    c1,c2,c3 = 0,0,0
    for i in range(n):
        a = answers[i]
        if a == ans1[i]: c1+=1
        if a == ans2[i]: c2+=1
        if a == ans3[i]: c3+=1

    answer = []
    M = max(c1,c2,c3)
    if M==c1: answer.append(1)
    if M==c2: answer.append(2)
    if M==c3: answer.append(3)

    return answer