from collections import Counter
def solution(k, tangerine):
    cnt=Counter(tangerine)
    cnt=sorted(cnt.items(), key=lambda x:(-x[1],x[0]))
    count=0
    v=[]
    for key, value in cnt:
        v.append(value)
    mv=max(v)
    if mv>k:
        count=1
    else:
        for i in range(len(v)):
            k-=v[i]
            count+=1
            if k<=0:
                break
    return count