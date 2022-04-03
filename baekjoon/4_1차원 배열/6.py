# 6
n = int(input())
answers = []
quiz = []
for i in range(n):
    x = input()
    quiz.append(x)
    


while quiz:
    q = quiz.pop(0)

    answer = 0
    cnt = 0
    for ans in q:
        if ans == 'O':
            cnt += 1
            answer += cnt
        else:
            cnt = 0
    answers.append(answer)

for ans in answers:
    print(ans)
        
            