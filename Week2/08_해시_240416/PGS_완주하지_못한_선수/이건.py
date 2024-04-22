# 아이디어
## 

# 예상 시간복잡도
##

# 풀이시간 
## 분

# 실행시간 
## 0.01ms~ 78.58ms
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()

    for i in range(len(participant)-1):
        if participant[i] != completion[i]:
            answer = participant[i]
            return answer
    if answer == '':
        answer = participant[-1]
    return answer