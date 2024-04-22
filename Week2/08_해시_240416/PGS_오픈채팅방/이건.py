# 아이디어
## 

# 예상 시간복잡도
##

# 풀이시간 
## 60분

# 실행시간 
## 0.02ms~ 70.52ms
def solution(record):
    answer = []
    dic = {}
    for i in record:
        arr = i.split(" ")
        if arr[0] != "Leave":
            dic[arr[1]] = arr[2]
            
    for i in record:
        arr = i.split(" ")
        if arr[0] == "Enter":
            answer.append(dic[arr[1]] + "님이 들어왔습니다.")
        elif arr[0] == "Leave":
            answer.append(dic[arr[1]] + "님이 나갔습니다.")
        
    return answer