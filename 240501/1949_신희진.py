from collections import deque


# 변수 명
# x,y = 현재위치
# K = 최대 공사 가능 깊이
# res =
def bfs(x, y, K):
    # 현재 위치 x,y / 등산로의 길이/ 최대 공사 가능 깊이 / 등산로 위치 정보 / 현재 등산로 높이
    Q = deque([(x, y, 1, K, [(x, y)], arr[x][y])])
    # 상 하 좌 우
    di = [0, -1, 1, 0]
    dj = [-1, 0, 0, 1]
    # vis = list([0 for _ in range(N)] for __ in range(N))
    # 최종 반환될 등산로의 거리
    max_dis = 0

    while Q:
        x, y, res, k, vis, bv = Q.popleft()
        # print(x,y,res,vis)
        max_dis = max(max_dis, res)
        # 상 하 좌 우 탐색
        for i in range(4):
            if 0 <= x + di[i] < N and 0 <= y + dj[i] < N:
                # 내가 가고자 하는 위치
                nx, ny = x + di[i], y + dj[i]
                # print(x,y,"nx,ny의 값 : ",nx,ny,arr[nx][ny], arr[x][y])

                # 가고자하는 위치의 등산로 높이가 현재 등산로 높이보다 낮고, 내가 간 곳이 아니라면
                if arr[nx][ny] < bv and (nx, ny) not in vis:
                    # print("들어갔니..? nx,ny,,?",nx,ny)
                    # 등산경로에 추가
                    new_vis = vis + [(nx, ny)]
                    # Q에 반환 > 현재 위치 / 등산로 거리 +1 / 최대 공사 가능 깊이 / 등산로 위치에 가고자하는 위치 추가/ 가고자하는 산 높이
                    Q.appendleft((nx, ny, res + 1, k, new_vis, arr[nx][ny]))

                # 가고자하는 위치의 등산로 높이가 현재 등산로 높이보다 높거나 같고, 최대 공사 가능 깊이가 있다면
                elif arr[nx][ny] >= bv and k > 0:
                    # 최소로 산을 깎음
                    m = abs(arr[nx][ny] - arr[x][y]) + 1
                    # 그 위치가 내가 간곳이 아니고, 깎았을때 0보다는 커야함
                    if k - m >= 0 and (nx, ny) not in vis and arr[nx][ny] - m >= 0:
                        # 경로 update
                        new_vis = vis + [(nx, ny)]
                        Q.appendleft((nx, ny, res + 1, 0, new_vis, arr[nx][ny] - m))
        else:
            continue
    return max_dis


T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 시작할 수 있는 좌표를 담을 start 큐
    start = deque()
    # 산의 최대 높이
    max_k = 0
    # 산의 최대 높이 구하기
    for i in arr:
        if max(i) >= max_k:
            max_k = max(i)
    # 시작 가능한 좌표 담기
    for x in range(N):
        for y in range(N):
            if arr[x][y] == max_k:
                start.append((x, y))
    # 최종 값 변수 설정
    result = 0
    # 시작 가능 좌표부터 bfs
    for x, y in start:
        # 값을 비교후 최종 result 도출
        if result <= bfs(x, y, K):
            result = bfs(x, y, K)
    print(f'#{tc + 1}', result)