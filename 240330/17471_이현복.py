import sys
sys.stdin = open('input1.txt','r')
from pprint import pprint
''' 
17471번_게리맨더링 
시간 : 176ms,76ms
메모리 : 114232KB,34112KB
'''


from collections import deque
def bfs(zone_data):                 # visited 안쓰고 했다가 무한루프 빠짐 
    if not zone_data[0]: return 0
    q=deque()
    q.append(zone_data[0][0])
    visited=[0]*(N)
    visited[zone_data[0][0]]=1
    cnt = 1
    while q:
        idx = q.popleft()
        for i in range(N):
            if arr[idx][i]==1 and i in zone_data[0] and visited[i] == 0:
                q.append(i)
                visited[i]=1
                cnt += 1
    return cnt
    

N=int(input())
data=list(map(int,input().split()))
arr = [[0]*N for _ in range(N)]
for i in range(N):
    tmp = list(map(int,input().split()))
    if tmp[0]:
        for j in tmp[1:]:                   # 1번 인덱스 이후부터 인접한 수를 주어진다
            arr[i][j-1]=arr[j-1][i] = 1     # 인접행렬 체크(양방향)
res = -1
for i in range(1<<N):               # 모든 경우를 다 구해보자
    if i > (i^int('1'*N,2)):        # xor연산으로 같은 구성에 팀만 바뀐 경우 스킵   
        a_zone = [[],0]
        b_zone = [[],0]
        for j in range(N):
            if i&(1<<j):
                a_zone[0].append(j)
                a_zone[1]+=data[j]
            else:
                b_zone[0].append(j)
                b_zone[1]+=data[j]
        if bfs(a_zone)+bfs(b_zone)==N:
            if res >=0:             # res > 0 이라고 했다가 시간 겁나 버림
                res = min(res,abs(a_zone[1]-b_zone[1]))
            else:
                res = abs(a_zone[1]-b_zone[1])
print(res)