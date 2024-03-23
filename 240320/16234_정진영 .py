"""
메모리 : 34244 KB
시간 : 5080 ms
"""


from collections import deque
def bfs(i,j):
    global cnt
    q = deque()
    union = [] # 연합 국가들의 좌표 리스트

    q.append((i,j))
    union.append((i,j))


    visited[i][j] =1 # 현재 좌표 방문 표시
    total = arr[i][j] # 현재 인구 업데이트
    cnt =1 # 카운트 현재 도시 포함

    check = False
    while q:
        x,y = q.popleft()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                tmp = abs(arr[x][y] - arr[nx][ny])  # 인구 차이
                if L <= tmp <= R:
                    check =True
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                    union.append((nx,ny))
                    total += arr[nx][ny]
                    cnt +=1
    avg = total // cnt
    for ux, uy in union:
        arr[ux][uy] = avg

    return check # 이동 여부 리턴


N, L, R = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

days = 0
while True :
    visited = [[0] * N for _ in range(N)]
    moved = False # 인구 이동 여부 확인
    for i in range(N):
        for j in range(N):
            if not visited[i][j] :
                if bfs(i, j):
                    moved = True
    if not moved:
        break
    days+=1

print(days)


