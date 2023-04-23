def solution(s):
    cnt_0=0
    cnt_2=0
    while True:
          total=0
          if s=='1':
                break
          else:
                for i in s:
                      if i=='0':
                            cnt_0+=1
                if cnt_0>0:
                      s=s.replace('0','')
                      for i in s:
                          total+=int(i)
                      s=bin(total)
                      s=s[2:]
                      cnt_2+=1
                else:
                      for i in s:
                            total+=int(i)
                      s=bin(total)
                      s=s[2:]
                      cnt_2+=1
    return [cnt_2, cnt_0]