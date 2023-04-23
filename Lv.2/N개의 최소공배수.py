def gcd(x,y):
    "최대공약수"
    while y:
        x,y=y,x%y
    return x

def lcm(x,y):
    "최소공배수"
    rst=(x*y)//gcd(x,y)
    return rst

def solution(arr):
    for i in range(len(arr)-1):
        arr[i+1]=lcm(arr[i],arr[i+1])
    return arr[-1]