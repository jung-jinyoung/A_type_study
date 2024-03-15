'''
백준 14503 로봇 청소기
메모리 31120kb
시간 40ms
'''
N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def clean(i, j, d):
    cnt = 0
    while True:
        # 청소하고 청소 횟수 1 증가
        if room[i][j] == 0:
            room[i][j] = 2 # 청소함
            cnt += 1

        # 반시계 방향으로 회전하며 청소하지 않은 칸 탐색
        for _ in range(4):
            d = (d + 3) % 4
            ni, nj = i + di[d], j + dj[d]
            # 범위 안이고, 청소 안 돼 있는 곳
            if 0 <= ni < N and 0 <= nj < M and room[ni][nj] == 0:
                # 이동했으면 다시 1번으로
                i, j = ni, nj
                break 

        else:
            # 주변이 모두 깨끗하다면 후진하거나 멈춤
            # 뒤를 보지말고 후진을 해라
            i, j = i + di[d] * -1, j + dj[d] * -1 # 후진
            # 범위 안인데 벽이거나, 범위 밖인 경우에
            if (0 <= i < N and 0 <= j < M and room[i][j] == 1):
                print(cnt)
                return

clean(r, c, d)
