def solution(citations):
    n_citations=sorted(citations)
    cnt=0
    for i in range(len(n_citations)):
        if n_citations[i]>=len(n_citations)-i:
            cnt+=1
    return cnt