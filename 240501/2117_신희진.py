def f(x, y, k):  # 시작 x,y,영역 k
    global res_home_cnt
    # 좌우 조사
    lr_i = [0, 0]
    lr_j = [-1, 1]
    # 위 아래 조사
    ud_i = [-1, 1]
    ud_j = [0, 0]

    # 방문 체크
    vis = list(list(0 for _ in range(N)) for __ in range(N))
    # 집 개수
    home_cnt = 0

    # 양옆으로 조사
    for i in range(2):
        # 영역만큼 좌 우로 나감
        for j in range(k):
            # 나갔을때 범위 안에 있는지 확인
            if 0 <= x + (lr_i[i]) * j < N and 0 <= y + (lr_j[i]) * j < N:
                nx = x + (lr_i[i]) * j
                ny = y + (lr_j[i]) * j
                # 방문한 적이 없고,
                if vis[nx][ny] == 0:
                    # 집이 있다면?
                    if arr[nx][ny] == 1:
                        # 집 개수 count
                        home_cnt += 1
                        vis[nx][ny] = 1
                # 좌 우에서 위아래로 탐색
                # 탐색은 좌 우로 점점 멀어질 수 록 -1 씩 해줘야함 > 마름모라서
                for ud in range(2):
                    for idx in range(k - j - 1, 0, -1):
                        # 내가 돈 곳이 범위내에 있다면
                        if 0 <= nx + (ud_i[ud]) * (idx) < N and 0 <= ny + (ud_j[ud]) * (idx) < N:
                            # 내가 갈 수 있는 곳임을 체크
                            nx_2 = nx + (ud_i[ud]) * (idx)
                            ny_2 = ny + (ud_j[ud]) * (idx)
                            # 방문하지 않았는지 체크
                            if vis[nx_2][ny_2] == 0:
                                vis[nx_2][ny_2] = 1
                                # 내가 간곳에 집이 있다면?
                                if arr[nx_2][ny_2] == 1:
                                    # 집 개수 count
                                    home_cnt += 1

    return home_cnt


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 최종 집의 개수
    res_home_cnt = 0
    # 0,0 부터 모두 탐색
    for x in range(N):
        for y in range(N):
            # 탐색 깊이
            for k in range(1, N + 2):
                # 손해가 아니면서
                if f(x, y, k) * M - (k * k + (k - 1) * (k - 1)) >= 0:
                    # 최대 개수 구하기
                    if res_home_cnt < f(x, y, k):
                        res_home_cnt = f(x, y, k)
    print(f'#{tc + 1}', res_home_cnt)