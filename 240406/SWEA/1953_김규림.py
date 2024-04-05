from collections import deque

di = [0, 1, 0, -1]           # 우하좌상
dj = [1, 0, -1, 0]

rev = [2, 3, 0, 1]            # 우하좌상 반대 방향 인덱스

tunnel = [[0, 0, 0, 0],       # 연결 가능한 방향
          [1, 1, 1, 1],
          [0, 1, 0, 1],
          [1, 0, 1, 0],
          [1, 0, 0, 1],
          [1, 1, 0, 0],
          [0, 1, 1, 0],
          [0, 0, 1, 1]]


def bfs(si, sj):
    visited = [[0] * M for _ in range(N)]
    visited[si][sj] = 1                     # 시작점 방문 표시
    Q = deque([(si, sj)])
    result = 1                              # 검거한 위치의 개수
    while Q:                                # 큐가 빌 때까지
        r, c = Q.popleft()
        for d in range(4):
            if tunnel[arr[r][c]][d] != 0:
                ni = r + di[d]
                nj = c + dj[d]
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 0 and visited[ni][nj] == 0:
                    if tunnel[arr[ni][nj]][rev[d]] != 0:        # 다음 위치의 터널이 반대 방향으로 연결 되어 있으면
                        if visited[r][c] + 1 > L:               # 시간이 L을 초과하면
                            return result
                        visited[ni][nj] = visited[r][c] + 1     # 현재 위치까지의 시간을 저장
                        Q.append((ni, nj))
                        result += 1                             # 검거한 위치의 개수 증가
    return result


# main
T = int(input())
for t in range(T):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t+1} {bfs(R, C)}')