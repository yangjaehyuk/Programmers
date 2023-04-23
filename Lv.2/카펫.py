def solution(brown, yellow):
    answer = []
    rst = brown+yellow
    garo = 0
    for i in range(3, rst+1):
        "세로"
        if rst % i == 0:
            answer.append(i)
    for j in answer:
        garo = rst/j
        "가로 = 합계 / 세로"
        if (garo-2) * (j-2) == yellow:
            return [garo, j]