"""
N * N 도시    빈 칸(0), 치킨집(2), 집(1) 중 하나이다.
r행 c열. r과 c는 1부터 시작

치킨거리 : 집과 '가장' 가까운 치킨집 사이의 거리.
치킨 거리는 집을 기준으로 정해지며, 각각의 집은 치킨 거리를 갖고 있다.
도시의 치킨 거리는 모든 집의 치킨 거리의 합

두 칸 사이의 거리는 abs(r1 - r2) + abs(c1 - c2)

수익 증가를 위해 일부 치킨집을 폐업.
가장 수익을 많이 낼 수 있는 치킨집의 개수는 최대 M개

도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 폐업시켜야 함.
어떻게 고르면 도시의 치킨 거리가 가장 작게 될지 구하라!
"""
import sys
sys.stdin = open("input.txt", "r")


# 도시의 치킨 거리 계산하는 함수
def cal(tlst):
    sm = 0
    for hi, hj in home:
        mn = 2 * N  # 초기 최소 거리 설정
        # 모든 집에 대해
        for ci, cj in tlst:
            # 현재 선택된 치킨집들과의 거리 중 최소값 계산
            mn = min(mn, abs(hi - ci) + abs(hj - cj))
        sm += mn  # 최소 거리를 누적하여 합산
    return sm


# 치킨집을 최대 M개 고르는 DFS 함수
def dfs(n, tlst):
    global ans
    if n == cnt:  # 치킨집을 모두 고른 경우
        if len(tlst) == M:  # M개의 치킨집을 선택한 경우
            ans = min(ans, cal(tlst))  # 치킨 거리를 계산하여 최소값 갱신
        return

    # 현재 치킨집을 선택하는 경우와 선택하지 않는 경우를 각각 탐색
    dfs(n + 1, tlst + [chicken[n]])  # 현재 치킨집을 선택
    dfs(n + 1, tlst)  # 현재 치킨집을 선택하지 않음


N, M = map(int, input().split())
arr = [[0] + list(map(int, input().split())) for _ in range(N)]     # 앞에 [0]을 추가해 인덱스 문제랑 맞추기
chicken = []
home = []
print(arr)
for i in range(1, N+1):
    for j in range(1, N+1):
        if arr[i][j] == 1:
            home.append((i, j))
        elif arr[i][j] == 2:
            chicken.append((i, j))

cnt = len(chicken)
ans = 2*N*2*N
dfs(0, [])


######################



# from itertools import combinations  # 조합을 생성하기 위한 모듈
#
# # 입력 받기
# graph = []  # 도시의 상태를 저장할 리스트
# n, m = map(int, input().split())  # 도시의 크기와 선택할 치킨집의 수 입력
# for _ in range(n):
#     graph.append(list(map(int, input().split())))  # 도시의 상태 입력하여 graph에 저장
#
# chicken = []  # 치킨집의 위치를 저장할 리스트
# house = []  # 가정집의 위치를 저장할 리스트
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 1:  # 가정집인 경우
#             house.append((i + 1, j + 1))  # house 리스트에 추가
#         elif graph[i][j] == 2:  # 치킨집인 경우
#             chicken.append((i + 1, j + 1))  # chicken 리스트에 추가
#
# result = n * 2 * len(house)  # 최소 치킨 거리를 구하기 위한 초기값 설정
# # 조합을 이용하여 치킨집을 m개 선택하는 모든 경우에 대해 치킨 거리 계산
# for comb in list(combinations(chicken, m)):
#     dist = 0  # 치킨 거리를 저장할 변수
#     for a, b in house:  # 모든 가정집에 대해
#         temp = n * 2  # 초기 최소 거리 설정
#         for x, y in comb:  # 선택된 치킨집들과의 거리 계산
#             temp = min(temp, abs(a - x) + abs(b - y))  # 가장 가까운 치킨집과의 거리 갱신
#         dist += temp  # 각 가정집의 최소 치킨 거리를 누적하여 합산
#     result = min(result, dist)  # 전체 최소 치킨 거리 갱신
#
# print(result)  # 최종 결과 출력