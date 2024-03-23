from collections import deque

def func(a, b, index):
    open = []                   # a, b와 연걸된 나라 담기
    open.append((a, b))

    q = deque()
    q.append((a, b))
    graph[a][b] = index         # 현재 연합에 번호 할당
    sum_num = arr[a][b]         # 현재 연합의 총 인구 수
    cnt = 1                     # 현재 연합의 국가 수

    while q:                    # q가 빌 때까지
        x, y = q.popleft()
        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]      # 주변 나라 확인
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == -1:
                if L <= abs(arr[x][y] - arr[nx][ny]) <= R:      # 인구 차이 확인
                    q.append((nx, ny))
                    graph[nx][ny] = index       # 현재 연합 번호 할당
                    sum_num += arr[nx][ny]      # 인구 수 누적
                    cnt += 1                    # 연합 국가 수 증가
                    open.append((nx, ny))       # 연합에 추가

    # 연합 국가 인구 분배하기
    for c, d in open:
        arr[c][d] = sum_num // cnt
    return cnt


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

total = 0       # 인구 이동 발생 횟수
# 인구 이동을 더 못할 때까지 반복
while True:
    graph = [[-1] * N for _ in range(N)]        # 연합 번호 기록
    idx = 0         # 연합 번호 초기화
    for i in range(N):
        for j in range(N):
            if graph[i][j] == -1:           # 해당 나라가 아직 처리되지 않았으면
                func(i, j, idx)
                idx += 1

    # 모든 국가가 연합 번호를 갖게 되는 시점
    if idx == N*N:
        break
    total += 1

print(total)