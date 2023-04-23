def solution(n):
    bn=bin(n)
    bn=bn[2:]
    cnt=0
    for i in bn:
        if i=='1':
            cnt+=1
    for j in range(n+1,1000001):
        cnt_1=0
        bi=bin(j)
        bi=bi[2:]
        for k in bi:
            if k=='1':
                cnt_1+=1
        if cnt==cnt_1:
            answer=j
            break
    return answer