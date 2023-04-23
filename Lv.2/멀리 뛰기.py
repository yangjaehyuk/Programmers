def solution(n):
    jump=[0,1,2]
    for i in range(3, n+1):
        jump.append(jump[i-1]+jump[i-2])
    return jump[n]%1234567