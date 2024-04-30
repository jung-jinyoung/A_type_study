'''
7 3
16 10 14 14 15 14 14
15 7 12 2 6 4 9
10 4 11 4 6 1 1
16 4 1 1 13 9 14
3 12 16 14 8 13 9
3 4 17 15 12 15 1
6 6 13 6 6 17 12
-> 7이 나와야 하는데 자꾸 6이 나와 ㅡㅡ
'''
def dfs(i, j):
    global K, maxLen, cut

    for di, dj in [(1, 0), (-1, 0), (0, -1), (0, 1)]: # 이동 방향 설정: 상, 하, 좌, 우
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N :
            if walkroad[ni][nj] < walkroad[i][j] and not visited[ni][nj]:
                visited[ni][nj] = visited[i][j] + 1
                dfs(ni, nj)
                maxLen = max(maxLen, visited[ni][nj])
                visited[ni][nj] = 0

            # 이동하려고 하는 칸이 현재 칸보다 크거나 같은 경우 (방문 한 적 없고 , 아직 길을 깎은 적 없음)
            if walkroad[ni][nj] >= walkroad[i][j] and not visited[ni][nj] and not cut:
                for k in range(1, K+1):
                    updated = walkroad[ni][nj] - k              # 현재 칸보다 작아질 때까지 깎아
                    if updated < walkroad[i][j]:
                        walkroad[ni][nj] = updated
                        cut = True                              # 깎을게
                        visited[ni][nj] = visited[i][j] + 1
                        dfs(ni,nj)                              # 다음으로 넘어갈게
                        visited[ni][nj] = 0

                        maxLen = max(maxLen, visited[ni][nj])

                        cut = False                             # 깎았던 거 취소하고 원래대로 돌려놓을게
                        walkroad[ni][nj] += k


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    walkroad = [list(map(int, input().split())) for _ in range(N)]

    highest = max(max(walkroad))            # 가장 높은 곳
    startpoint = []                         # 가장 높은 곳 리스트
    for i in range(N):
        for j in range(N):
            if walkroad[i][j] == highest:
                startpoint.append((i,j))

    maxLen = 0
    cut = False

    for i,j in startpoint:
        visited = [[0] * N for _ in range(N)]
        dfs(i, j)

    print(f'#{tc} {maxLen + 1}')                           # 시작점의 visited가 0이기 때문에 마지막에 +1을 해주어야 함