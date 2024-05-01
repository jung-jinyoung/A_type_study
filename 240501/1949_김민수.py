"""
등산로를ㄹ 만드는 규칙
1. 등산로는 가장 높은 봉우리에서 시작
2. 반드시 높은 지형에서 낮은 지형으로 가로 또는 세로 방향으로 연결
-> 높이가 같은 곳, 대각선 불가능
3. 한 곳을 정해 K 길이만큼 지형을 깎는 공사를 할 수 있음
"""
di = [-1, 1, 0, 0]
dj = [0, 0, 1, -1]

def dfs(i, j, cnt, work):
    global max_len
    if max_len < cnt:
        max_len = cnt

    for k in range(4):
        ni, nj = i+di[k], j+dj[k]
        if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0:
            if tops[i][j] > tops[ni][nj]:
                visited[ni][nj] = 1
                dfs(ni, nj, cnt+1, work)
                # 방문 표시 초기화
                visited[ni][nj] = 0     # 백트래킹 -> 방문표시 초기화

            elif tops[i][j] <= tops[ni][nj]:
                for k in range(1, K+1):
                    if work == 1 and tops[ni][nj] - k < tops[i][j]:
                        visited[ni][nj] = 1
                        tops[ni][nj] -= k   # 봉우리 깎기
                        dfs(ni, nj, cnt+1, work-1)
                        visited[ni][nj] = 0     # 백트래킹 -> 방문표시 초기화
                        tops[ni][nj] += k       # 깎은 봉우리 복구


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    tops = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    max_len = 0 # 등산로 최대 길이
    m_top = 0   # 가장 높은 봉우리

    # 최대 높이 구하기
    for p in range(N):
        for q in range(N):
            if m_top < tops[p][q]:
                m_top = tops[p][q]

    # 최대 높이와 같은 봉우리들의 위치 넣기
    for k in range(N):
        for l in range(N):
            if tops[k][l] == m_top:
                visited[k][l] = 1
                dfs(k, l, 1, 1)
                visited[k][l] = 0   # 방문표시 초기화  -> 이거 못해서 30분 더 걸림

    print(f'#{tc} {max_len}')