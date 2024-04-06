"""
탈주범이 있을 수 있는 위치의 개수 계산, 시간당 1의 거리 이동
위치 인덱스 : 2차원 리스트 인덱스, 탈주범 이동 후 그 자리에서 계속 있을 수 있음

접근 방법
    : BFS로 총 시간 안에 움직일 수 있는 인접 정점의 개수를 모두 구하기

    * 이동할 수 있는 인접 파이프 : 연결 여부 확인

메모리 : 50656 KB
기담 : 390 ms

"""
from collections import deque
#상, 우, 하, 좌
di = [-1,0,1,0]
dj = [0,1,0,-1]

# 터널 타입별 이동할 수 있는 델타 인덱스 저장 (더미 생성)
move_info = [
    [0],[0,1,2,3],[0,2],[1,3],[0,1],[1,2],[2,3],[0,3]
]

cd = [2,3,0,1] # 확인해야 할 인덱스 저장
def linked_check(next,turn):
    op_k = cd[turn]
    if op_k  in move_info[next]:
        return True # 연결되어 있으면
    return False # 그렇지 않다면:


# 맨홀 위치에서부터 bfs, 시간 동안 갈 수 있는 인접 정점 위치 개수 카운트
def bfs(i,j,l): # 현재 맨홀 위치 (i,j) 총 시간 l

    q = deque()

    # 현재 맨홀 위치 저장
    q.append((i,j))
    visited[i][j] = 1 # 현재 맨홀 위치 저장

    while q :
        x, y = q.popleft()
        if visited[x][y] == l: # 주어진 시간과 같으면
            continue
        n = ground[x][y] # 파이프 정보
        for turn in move_info[n]:
            # 이동할 위치
            nx = x + di[turn]
            ny = y + dj[turn]

            # 배열에서 벗어나지 않거나 연결된 파이프가 있으면
            if (0<=nx<N and 0<=ny<M) and not visited[nx][ny] and ground[nx][ny] :
                next = ground[nx][ny]
                # 연결 확인
                if linked_check(next,turn):
                    visited[nx][ny]= visited[x][y]+1
                    q.append((nx,ny))


def check():
    global ans
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                ans+=1

T = int(input())
for tc in range(1,T+1):
    N, M, R, C, L = map(int,input().split())
    # M*N 2차원 리스트
    # 현재 탈주범 위치 C*R

    ground = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    # 맨홀 위치에서부터 bfs, 시간 동안 갈 수 있는 인접 정점 위치 개수 카운트

    visited = [[0]*M for _ in range(N)] # 방문 위치 리스트
    bfs(R,C,L)

    check()
    print(f'#{tc} {ans}')