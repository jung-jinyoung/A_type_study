from collections import  deque

def bfs(si, sj, N, M):
    # si, sj 에서 출발해서 N,M 도착할 때 까지의 최소 칸 수
    visited = [[0] * M for _ in range(N)]
    q = deque()

    # 시작 점 방문
    q.append((si,sj))
    visited[si][sj] = 1


    while q :
        i, j = q.popleft()
        if (i, j) == (N-1, M-1):
            return visited[i][j]
        for di, dj in [(0,1),(1,0),(0,-1),(-1,0)]:
            ni = i + di
            nj = j + dj
            if 0<=ni<N and 0<=nj<M and not visited[ni][nj] and maze[ni][nj] != '0':
                q.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1 # 방문한 횟수 추가



N, M =map(int,input().split())
maze = [input() for _ in range(N)]
si, sj = 0,0 # (1,1)에서 출발

print(bfs(si,sj,N,M))