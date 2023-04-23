def solution(n):
    ans=1
    while True:
        if n//2==0:
            break
        if n%2==1:
            ans+=1
            n//=2
        else:
            n//=2
    return ans