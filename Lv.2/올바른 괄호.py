from collections import deque
def solution(s):
    cnt=0
    rst=deque(s)
    if rst[0]==')':
        return False
    else:
        while rst:
            i=rst.popleft()
            if i ==')':
                cnt-=1
                if cnt<0:
                    return False
            else:
                cnt+=1
    if cnt==0:
        answer=True
    else:
        answer=False
    return answer