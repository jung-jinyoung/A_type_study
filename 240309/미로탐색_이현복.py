# 2178_미로 탐색
'''
https://www.acmicpc.net/problem/2178
'''
from collections import deque

def bfs(iii,jjj):               # 시작점 좌표 iii,jjj
    visited[iii][jjj] = 1
    queue.append([iii,jjj])     # 큐에 넣고 시작
    while queue:
        i,j = queue.popleft()   
        if i == N-1 and j == M-1:
            print(visited[i][j])    # 큐 순서상 처음 목표값에 오면 종료 
            return
        for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            ni,nj = i+di,j+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == '1' and visited[ni][nj] == 0:
                queue.append((ni,nj))
                visited[ni][nj] = 1 + visited[i][j] # visited로 횟수 카운팅

N,M = map(int,input().split())
arr = [input() for _ in range(N)]
visited = [[0]*M for _ in range(N)]
queue = deque()
bfs(0,0)