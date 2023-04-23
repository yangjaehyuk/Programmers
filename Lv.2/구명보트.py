from collections import deque
def solution(people, limit):
    lst=deque(sorted(people))
    cnt=0
    while True:
        if len(lst)==0:
            break
        if len(lst)>1:
          if lst[0]+lst[-1]<=limit:
              lst.pop()
              lst.popleft()
              cnt+=1
          else:
              lst.pop()
              cnt+=1
        else:
            lst.pop()
            cnt+=1
    return cnt