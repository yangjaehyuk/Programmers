def solution(s):
    new_s = s.replace('"', '')
    lst_s = list(map(int, new_s.split(" ")))
    rst = []
    for i in lst_s:
        rst.append(i)
    answer = str(min(rst))+" "+str(max(rst))
    return answer