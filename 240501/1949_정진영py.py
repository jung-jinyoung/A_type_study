"""
접근 방법 : DFS ( N의 범위가 작고, 기저 조건들이 많기 때문에 )

1. 시작점을 찾기 위한 높은 봉우리 찾기 -> 해당 좌표에서 등산로 조성 탐색
2. 탐색 시 방문 표시 : * 탐색 후 초기화 과정을 하지 않아서 틀렸음*
3. 더 이상 방문할 곳이 없을 때 : 공사 진행 여부 확인 -> 공사를 하지 않았으면 공사 후 탐색 *역시 초기화 과정 필요*
4. 최대 등산로 길이는 재귀 함수 계속 업데이트 : 등산로 길이 == 현재 방문 좌표

메모리 : 52360 KB
시간 : 213 ms

"""


# 상, 하, 좌, 우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 등산로 조성 함수
def construct_trail(x, y, cutting): # 현재 위치 (x,y) 에서공사 여부 cutting 확인
    global max_length

    # 등산로 길이 업데이트
    max_length = max(max_length,visited[x][y])

    # 현재 위치에서 이동할 수 있는 방향 탐색
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        # 다음 위치가 범위 내에 있고 방문하지 않았다면 이동 가능
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            # 다음 위치의 높이가 현재 위치보다 낮다면 그대로 이동
            if heights[nx][ny] < heights[x][y]:
                visited[nx][ny] = visited[x][y] + 1
                construct_trail(nx, ny, cutting)
                # 초기화
                visited[nx][ny] = 0

            # 다음 위치의 높이가 현재 위치보다 높은 경우
            elif heights[nx][ny] - K < heights[x][y] and not cutting:
                # 공사를 할 수 있는 깊이 만큼 공사하고 이동
                diff = heights[nx][ny] - heights[x][y]
                heights[nx][ny]-= diff+1
                visited[nx][ny] = visited[x][y]+1
                construct_trail(nx, ny, True)

                # 초기화
                heights[nx][ny] += diff+1
                visited[nx][ny] = 0


# 테스트 케이스 수 입력
T = int(input())

# 테스트 케이스별로 실행
for tc in range(1, T + 1):
    # 지도의 크기 N과 최대 공사 가능 깊이 K 입력
    N, K = map(int, input().split())

    # 지도 정보 입력
    heights = [list(map(int, input().split())) for _ in range(N)]
    top_height = 0

    # 최고 높이 찾기
    for i in range(N):
        for j in range(N):
            if heights[i][j] > top_height:
                top_height = heights[i][j]

    # 최장 등산로의 길이 초기화
    max_length = 0
    # 방문 표시 리스트 초기화
    visited = [[0] * N for _ in range(N)]

    # 최고 높이에서 탐색하여 등산로 조성
    for i in range(N):
        for j in range(N):
            if heights[i][j] == top_height:
                visited[i][j] =1
                # 각 지점을 시작점으로 등산로 조성
                construct_trail(i, j, False)
                # 초기화
                visited[i][j] = 0

    print(f'#{tc} {max_length}')
