# 7576번_토마토
'''
https://www.acmicpc.net/problem/7576
'''

from collections import deque

M,N = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
q = deque()
day = 1                         # while 문에 들어가지 않을경우를 위한 day
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:      # 익은 토마토 좌표를 append
            q.append((i,j))

while q:                        # 큐에 담긴 좌표들을 모두 처리 할 때까지
    i,j = q.popleft()
    for di,dj in [(0,1),(0,-1),(1,0),(-1,0)]:   # 델타
        ni, nj = i + di, j + dj
        if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0:    # 주어진 범위 내에 위치 +  안익은 토마토
            q.append((ni,nj))                           # 전염 되어 익었으니 좌표 append
            arr[ni][nj]=arr[i][j]+1                     # 몇번째 day인지를 알기 위해서 전염시킨 토마토 자리의 값에 1을 도해서 저장
            day = arr[ni][nj]
            
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:         # 0이 하나라도 있으면 실패
            day = 0
            break
    if not day: break
print(day-1)                       # 시작이 1이었으니 빼주자