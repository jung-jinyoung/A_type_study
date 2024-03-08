import sys # 시간초과로 인해 import sys
from collections import deque # bfs로 풂, deque 사용
m,n,h = map(int,input().split()) # mn크기, h상자수
graph = []
queue = deque([]) # 익은 토마토의 좌표 값을 담을 deque 생성

for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int,sys.stdin.readline().split()))) # 2중 리스트
        for k in range(m):
            if tmp[j][k]==1: # 익은 토마토의 좌표값 append
                queue.append([i,j,k])
    graph.append(tmp)
    
dx = [-1,1,0,0,0,0] # 상,하,좌,우,아래층,위층
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
while(queue):
    x,y,z = queue.popleft() # queue 의 왼쪽부터 꺼내옴
    
    for i in range(6):
        a = x+dx[i]
        b = y+dy[i]
        c = z+dz[i]
        # 좌표가 범위내에 있고 익지 않은 토마토면 
        if 0<=a<h and 0<=b<n and 0<=c<m and graph[a][b][c]==0: 
            # queue 에 append
            queue.append([a,b,c])
            # 1씩 늘려가며 방문표시
            graph[a][b][c] = graph[x][y][z]+1
            
day = 0
for i in graph:
    for j in i:
        for k in j:
            if k==0: # 익지 않은 토마토가 있으면 
                print(-1) 
                exit(0)
        day = max(day,max(j))
print(day-1)