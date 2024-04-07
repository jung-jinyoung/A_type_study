
'''
어떤 배추에 지렁이가 살고 있으면 인접한 배추로 이동 가능
0은 배추가 심어져 있지 않은 땅
1은 배추가 심어져있는 땅
배추가 몇 군데 퍼져있는지 조사
T 테스트 케이스
M N K
K줄에 걸쳐서 배추의 위치 X Y
'''
from collections import deque

def bfs(si, sj):
    q = deque([])
    q.append((si, sj))
    visited[si][sj] = 1
    while q :
        # 방문한 적이 없고, 인접한 칸 중 1이 있는 경우에만
        i, j = q.popleft()
        for di, dj in ((1,0), (-1,0), (0,1), (0,-1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and arr[ni][nj] == 1:
                q.append((ni, nj))
                visited[ni][nj] = 1


T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    for _ in range(K):
        j, i= map(int, input().split())
        arr[i][j] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and arr[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)