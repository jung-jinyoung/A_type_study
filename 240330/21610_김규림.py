N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
move = [list(map(int, input().split())) for _ in range(M)]

cloud = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]        # 구름 초기 위치 나타냄
di = [0, -1, -1, -1, 0, 1, 1, 1]            # 구름 이동 방향
dj = [-1, -1, 0, 1, 1, 1, 0, -1]

dx = [-1, -1, 1, 1]     # 대각선 이동 방향
dy = [-1, 1, 1, -1]

for d, s in move:       # 이동 리스트에서 방향 = d, 거리 = s 가져옴
    move_cloud = []
    for i, j in cloud:                  # 구름의 현재 위치에서 각 구름을 가져옴
        ni = (i + di[d-1] * s) % N      # 이동 방향과 거리를 기반으로 구름 이동
        nj = (j + dj[d-1] * s) % N
        arr[ni][nj] += 1                # 이동한 위치 물의 양 증가
        move_cloud.append((ni, nj))     # 이동된 구름 추가

    for a, b in move_cloud:
        cnt = 0
        for k in range(4):              # 이동된 구름 위치에서 대각선 4방향 확인
            na = a + dx[k]
            nb = b + dy[k]
            if 0 <= na < N and 0 <= nb < N and arr[na][nb] > 0:
                cnt += 1                # 0보다 크면 1 추가

        arr[a][b] += cnt                # 해당 위치에 cnt 값 더해주기

    new_cloud = []                      # 새로운 구름 리스트 생성
    for c in range(N):
        for d in range(N):
            if (c, d) in move_cloud or arr[c][d] < 2:
                continue                # 이동 구름 or 2보다 작으면 continue
            arr[c][d] -= 2              # 아니면 -2
            new_cloud.append((c, d))    # 새로운 구름 추가
    cloud = new_cloud                   # new_cloud를 cloud로

total = 0           # 물의 총합 구하기
for p in range(N):
    for q in range(N):
        total += arr[p][q]

print(total)