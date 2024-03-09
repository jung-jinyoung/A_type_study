from collections import deque

def bfs():
    global day
    while q:
        i, j = q.popleft()
        for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and tomato[ni][nj] == 0:
                q.append((ni, nj))
                tomato[ni][nj] = tomato[i][j] + 1
                day = tomato[ni][nj]
                
# 진영언니 말대로 break나 exit() 안 쓰고 해보려고 daycnt 함수 만들었어용
def daycnt():
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 0:
                return False
    return True

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
day = 1
q = deque()
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            q.append((i, j))
bfs()
if daycnt() == True:
    print(day - 1)
else:
    print(-1)
