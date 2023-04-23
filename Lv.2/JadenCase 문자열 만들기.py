def solution(s):
    lst=list(s)
    small_lst=s.lower()
    lst_small=list(small_lst)
    lst_small[0]=lst[0].upper()

    for i in range(len(lst_small)-1):
        if lst[i]==' ':
            lst_small[i+1]=lst[i+1].upper()

    lst_small=''.join(lst_small)
    return lst_small