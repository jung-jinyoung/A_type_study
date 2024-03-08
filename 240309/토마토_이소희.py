# 실패한 코드이지만.... 나으 노력을 알아조

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
def bfs(s_i, s_j):
    next = [(s_i, s_j)]
    visited[s_i][s_j] = 0
    while next:
        i, j = next.pop(0)
        # 4방향, 범위내, 미방문, tomato[] == 0
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and tomato[ni][nj] == 0:
                next.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
                tomato[ni][nj] = 1

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

# 1. 다 익은 토마토가 있는 경우를 구분하기 위한 flag1
flag1 = False
for k in range(N):
    # 1-1. 0이 없으면 (이미 다 익어있으면) flag1 = True가 됨
    if 0 not in tomato[k]:
        flag1 = True
    # 1-2. 안 익은 토마토가 있으면 flag1 = False
    else:
        flag1 = False
        break

startList = []
# 2. 안 익은 토마토가 있는 경우라면
# 2-1. 1로 시작된 점을 startList에 담아    
if flag1 == False:
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 1:
                startList.append((i,j))
# 3. 각각의 시작점에 대하여 bfs
for each in startList:
    s_i, s_j = each
    bfs(s_i, s_j)

# 4. bfs를 다 돌고난 후에 visited 배열에 대하여
flag2 = False
max_v = 0
# 4-1. (1-1)의 경우일 때에 0을 print
if flag1 == True:
    print(0)
# 4-2. 안 익은 토마토가 있어서 시간에 따라 결과가 달라지는 경우라면
else:
    for i in range(N):
        for j in range(M):
            # 4-2-1. 다 돌았는데도 안 익은 토마토가 있으면
            if tomato[i][j] == 0:
                # flag = True로 바꾸고 -1을 print
                flag2 = True
                print(-1)
            if visited[i][j] > max_v:
                max_v = visited[i][j]
    # 4-2-2. 다 돌았을 때 모든 토마토가 익은 경우엔
    # visited배열에서 가장 큰 값을 출력
    if flag2 == False:
        print(max_v)
