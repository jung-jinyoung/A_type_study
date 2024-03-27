
'''
21610번_마법사 상어와 비바라기
시간 : 204/428ms
메모리 : 117580/34148KB
'''

# 비바라기 시전시 (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름 [좌하단 네칸]
# 구름이동 m번 , 방향 d와 s칸 이동
import sys
input = sys.stdin.readline
from collections import deque
delta=((0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1))
N,M=map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
cloud = deque([[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]])
move = [tuple(map(int,input().split())) for _ in range(M)]
for m in range(M):
    cloud_length = len(cloud)
    d,s=move[m][0],move[m][1]
    # 1&2단계
    for _ in range(cloud_length):
            i, j = cloud.popleft()
            i = (i + delta[d-1][0] * s) % N
            j = (j + delta[d-1][1] * s) % N
            cloud.append([i, j])
            arr[i][j] += 1
    # 3단계 구름 초기화

    # 4단계 물 복사 버그
    cloud_past = [[0]*N for _ in range(N)]
    for k in range(cloud_length):
        i,j=cloud[k]
        cloud_past[i][j]=1
        cnt = 0
        for a,b in [(1,1),(-1,-1),(-1,1),(1,-1)]:
            ni,nj=i+a,j+b
            if 0<=ni<N and 0<=nj<N and arr[ni][nj]!=0:
                cnt+=1
        arr[i][j]+=cnt
    # 5단계 
    for i in range(N):
        for j in range(N):
            if arr[i][j]>=2 and cloud_past[i][j]!=1:
                arr[i][j]-=2
                cloud.append([i,j])
    for i in range(cloud_length):
        cloud.popleft()
print(sum(sum(i) for i in arr))
