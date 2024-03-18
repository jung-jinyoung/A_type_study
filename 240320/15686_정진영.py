"""
치킨집들 중 M개를 선택하여 나올 수 있는 도시 치킨 거리의 합을 더함
가장 작은 도시 치킨 거리의 합을 산출
-> 브루트포스로 구현 (백트래킹 X)

시간 : 376 ms (Python3)
메모리 : 31120 KB
"""

# M개의 치킨집들의 도시 치킨 거리의 합 구하기
def sum_dist(arr):
    total = 0 # 햔제 선택한 치킨집들의 도시 치킨 거리의 합

    for i in range(N):
        for j in range(N):
            if city[i][j] == 1 : # 집을 찾아서 치킨집들 비교
                request = 200
                for tmp in arr:
                    d = abs(i-tmp[0]) + abs(j-tmp[1])
                    if request > d:
                        request = d
                total += request
    return total

# 치킨집들 중 중복 없이 M개를 선택
def check(c,i):
    global min_v

    if c == M: # M개를 선택했을 경우
        now = sum_dist(result) # 거리 구하기
        distances.append(now) # 리스트 저장
        return

    for i in range(i,len(stores)):
            result.append(stores[i])
            check(c+1,i+1)
            result.pop() # 초기화

import sys
input = sys.stdin.readline

N, M = map(int,input().split())
# 도시 정보: 집이면 1, 치킨집이면 2
city = [list(map(int, input().split())) for _ in range(N)]

# 치킨집 찾기
stores = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            stores.append((i,j))



result = [] # M개의 치킨집 저장 리스트
distances = [] # 모든 경우의 수의 치킨 거리 합 저장 리스트 초기화
check(0,0)
print(min(distances)) # 최소 도시 치킨 거리 출력