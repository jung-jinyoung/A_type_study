N, M = map(int, input().split())
x, y, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 방향별 이동 좌표 설정
di = [-1, 0, 1, 0]  # 북, 동, 남, 서
dj = [0, 1, 0, -1]

# 현재 위치를 청소, 청소한 칸의 수 저장
cnt = 0
if arr[x][y] == 0:
    arr[x][y] = 2
    cnt += 1

while True:
    cleaned = False
    for _ in range(4):
        # 현재 방향에서 왼쪽(반시계 90`) 방향으로 회전
        d = d - 1
        if d == -1:
            d = 3
        ni = x + di[d]
        nj = y + dj[d]
        # 왼쪽 방향에 아직 청소하지 않은 공간이 있다면 청소하고 이동
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
            arr[ni][nj] = 2
            cnt += 1
            x, y = ni, nj
            cleaned = True
            break

    # 네 방향 모두 청소가 되어있음
    if cleaned == False:
        if d == 2 or d == 3:  # 후진 방향
            back_d = d - 2
        elif d == 0 or d == 1:
            back_d = d + 2
        ni = x + di[back_d]
        nj = y + dj[back_d]

        # 후진할 수 있다면 후진하고
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 1:
            x, y = ni, nj       # x, y로 가서 네 방향 다시 탐색
        else:                   # 아니면 작동 중단
            break

print(cnt)
