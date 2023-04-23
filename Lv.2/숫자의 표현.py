def solution(n):
    cnt=0
    for i in range(1,n//2+1):
        total=0
        for j in range(i,n+1):
          total+=j
          if total==n:
              cnt+=1
          elif total>n:
              break
          
    return cnt+1