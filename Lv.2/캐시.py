from collections import deque
def solution(cacheSize, cities):
    "LRU : 가장 오랫동안 참조되지 않은 페이지를 교체"
    n_cities=[]
    for i in cities:
        n_cities.append(i.upper())
    d_cities=deque()
    i=0
    rst=0
    if cacheSize==0:
        rst=len(cities)*5
    else:
        while len(d_cities)!=cacheSize:
            if n_cities[i] in d_cities:
                rst+=1
                d_cities.remove(n_cities[i])
                d_cities.append(n_cities[i])
            else:
                rst+=5
                d_cities.append(n_cities[i])
            i+=1
        for j in range(i, len(n_cities)):
            if n_cities[j] in d_cities:
                rst+=1
                d_cities.remove(n_cities[j])
                d_cities.append(n_cities[j])
            else:
                rst+=5
                d_cities.popleft()
                d_cities.append(n_cities[j])
    return rst


# print(solution(	5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA","SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
