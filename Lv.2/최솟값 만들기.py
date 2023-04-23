from collections import deque
def solution(a,b):
    a.sort()
    b.sort()
    a=deque(a)
    b=deque(b)
    total=0
    min_rst=0
    while True:
      if len(a)==0 and len(b)==0:
          break
      if a[0]<b[0]:
          min_rst=a[0]
          total+=min_rst*b[len(b)-1]
          a.popleft()
          b.pop()
      else:
          min_rst=b[0]
          total+=min_rst*a[len(a)-1]
          b.popleft()
          a.pop()
    return total