from collections import deque
def solution(s):
    stack=[]
    deq=deque(s)
    cnt=0
    flag=False
    for _ in range(len(deq)):
      for i in deq:
          if i=='(' or i=='[' or i=='{':
              stack.append(i)
          else:
              if len(stack)>0:
                  if stack[-1]=='(' and i==')':
                      stack.pop()
                      flag=True
                  elif stack[-1]=='[' and i==']':
                      stack.pop()
                      flag=True
                  elif stack[-1]=='{' and i=='}':
                      stack.pop()
                      flag=True
      if not stack and flag==True:
        cnt+=1
      flag=False
      stack=[]
      deq.append(deq.popleft())
    return cnt