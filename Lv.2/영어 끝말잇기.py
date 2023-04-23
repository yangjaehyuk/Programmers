def solution(n, words):
    answer=[0,0]
    cnt=0
    used=[]
    used.append(words[0])
    for i in range(1, len(words)):
        cnt+=1
        if words[i][0]==used[i-1][-1] and words[i] not in used:
            used.append(words[i])
        else:
            answer[0]=cnt%n+1
            "탈락번호"
            answer[1]=cnt//n+1
            "탈락순서"
            break
    return answer