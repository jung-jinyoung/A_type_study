"""
N x N 크기의 땅. 각각의 땅에는 나라가 하나씩 존재.
나라에는 A[r][c]명이 살고 있음. 인접한 나라 사이에는 국경선이 존재. 인구 이동이 없을 때까지 지속

- 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 염
- 위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작
- 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 함.
- 연합을 이루고 있는 각 칸의 인구수는(연합의 인구수)/(연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
- 연합을 해체하고, 모든 국경선을 닫는다.

각 나라의 인구수가 주어졌을 때, 인구 이동이 며칠동안 발생하는지 구하는 프로그램을 작성하시오.
"""
import sys
sys.stdin = open("input.txt", "r")

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0

# 너비 우선 탐색을 통해 연합 형성
def bfs(x, y):
    q = deque()
    q.append((x, y))  # 시작점을 큐에 추가
    visited[x][y] = 1  # 방문 여부 표시
    union = [(x, y)]  # 연합을 이루는 나라들의 좌표를 저장하는 리스트

    while q:
        x, y = q.popleft()  # 큐에서 좌표를 하나 꺼냄

        # 상하좌우 이동
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            # 인접한 위치가 유효하고, 방문하지 않았으며, 인구 이동 조건에 부합하는 경우
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(country[nx][ny] - country[x][y]) <= r:  # 두 나라의 인구 차이
                    q.append((nx, ny))  # 큐에 인접한 나라의 좌표 추가
                    visited[nx][ny] = 1  # 방문 여부 표시
                    union.append((nx, ny))  # 연합을 이루는 나라들의 좌표에 추가

    return union


n, l, r = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(n)]

while True:
    visited = [[0] * n for _ in range(n)]  # 방문 여부 초기화
    move = 0  # 인구 이동이 발생했는지 여부를 나타내는 변수

    # 모든 나라에 대해 탐색
    for x in range(n):
        for y in range(n):
            if not visited[x][y]:  # 방문하지 않은 나라인 경우
                union = bfs(x, y)  # 현재 나라를 포함한 연합 형성

                if len(union) > 1:  # 연합이 형성된 경우
                    move = 1  # 인구 이동 발생 여부 표시
                    # 연합에 속한 나라들의 총 인구수 계산하여 평균 인구수 구함
                    population = sum(country[i][j] for i, j in union) // len(union)

                    # 연합에 속한 모든 나라의 인구수를 평균 인구수로 변경
                    for i, j in union:
                        country[i][j] = population

    # 인구 이동이 더 이상 발생하지 않는 경우 종료
    if not move:
        break
    cnt += 1  # 인구 이동이 발생했을 경우 날짜 카운트 증가

print(cnt)