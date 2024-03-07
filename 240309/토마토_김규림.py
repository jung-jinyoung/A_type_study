import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

q = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i, j))


while q:
    a, b = q.popleft()
    for k in range(4):
        ni = a + di[k]
        nj = b + dj[k]
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
            arr[ni][nj] = arr[a][b] + 1
            q.append((ni, nj))

result = 0
for line in arr:
    for tomato in line:
        if tomato == 0:
            print(-1)
            exit()
    result = max(result, max(line))
print(result-1)     # 1에서 시작해서 -1


