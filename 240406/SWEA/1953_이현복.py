import sys
sys.stdin = open('input1.txt','r')

'''
SWEA_1953_탈주범 검거
시간 : 186 ms
메모리 : 49,868 kb
'''
from collections import deque

# 상하좌우 순서 무조건!!
delta=((-1,0),(1,0),(0,-1),(0,1))
way=((1,2,5,6),(1,2,4,7),(1,3,4,5),(1,3,6,7))
road = (
    (),
    (0,1,2,3),
    (0,1),
    (2,3),
    (0,3),
    (1,3),
    (1,2),
    (0,2)
)

def bfs():
    visited = [[0]*M for _ in range(N)]
    q = deque()
    q.append((R,C))
    visited[R][C]=1
    cnt = 1
    while q:
        x,y=q.popleft()
        for i in road[arr[x][y]]:
            di,dj=delta[i]
            ni,nj=di+x,dj+y
            if 0<=ni<N and 0<=nj<M and visited[ni][nj]==0 and arr[ni][nj] in way[i]:
                visited[ni][nj]+=visited[x][y]+1
                if visited[ni][nj]==(L+1):
                    return cnt
                q.append((ni,nj))
                cnt+=1
    return cnt

T = int(input())
for tc in range(T):
    N,M,R,C,L = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    print(f'#{tc+1} {bfs()}')