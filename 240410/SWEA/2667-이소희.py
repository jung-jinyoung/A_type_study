'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''
from collections import deque

def bfs(si, sj):
    cnt = 1             # si, sj 칸 세고 시작
    q = deque([])
    q.append((si,sj))   # q에 si, sj 추가
    visited[si][sj] = 1 # 방문처리 하고
    while q:
        i, j= q.popleft()   # i, j 는 q에서 뽑아와
        for di, dj in ((1,0), (-1,0), (0,1), (0,-1)):
            ni, nj = i + di, j + dj
            # ni, nj가 범위 안에 있고, town[ni][nj]가 1이고, 아직 방문전이면 q에 추가
            if 0 <= ni < N and 0 <= nj < N and town[ni][nj] =='1' and not visited[ni][nj]:
                q.append((ni,nj))
                visited[ni][nj] = 1 # 방문처리 하고
                cnt += 1            # cnt 하나 더해
    return cnt

N = int(input())
town = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
# print(town)
ans = 0
num = []
for i in range(N):
    for j in range(N):
        if town[i][j] =='1' and not visited[i][j]:
            num.append(bfs(i,j))
            ans += 1
num.sort()
print(ans, *num, sep = '\n')

