
def solution(progresses, speeds):
    ans = []
    while progresses:
        print(progresses)
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        cnt = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt+=1

        if cnt != 0:
            ans.append(cnt)

    return ans
solution(progresses, speeds)