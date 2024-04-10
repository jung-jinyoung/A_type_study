from collections import deque

# 적록색약이 아닌 사람이 보는 구역 // 다 구분
def type1(si, sj):
    q1 = deque()
    q1.append((si,sj))
    visited1[si][sj] = 1
    while q1:
        i, j = q1.popleft()
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni, nj = i + di, j + dj
            # ni, nj가 범위내에 있고, bd[ni][nj]가 bd[i][j]랑 같을 때에만 탐색을 계속
            if 0 <= ni < N and 0 <= nj < N and bd[ni][nj] == bd[i][j] and not visited1[ni][nj]:
                q1.append((ni,nj))
                visited1[ni][nj] = 1

# 적록색약인 사람이 보는 구역 // R과 G를 같게 봄
def type2(si, sj):
    q2 = deque()
    q2.append((si,sj))
    visited2[si][sj] = 1
    while q2:
        i, j = q2.popleft()
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni, nj = i + di, j + dj
            # 적록색약에게 R == G
            if 0 <= ni < N and 0 <= nj < N and not visited2[ni][nj] :
                if (bd[i][j] == 'R' and (bd[ni][nj] == 'R' or bd[ni][nj] == 'G')) or (bd[i][j] == 'G' and (bd[ni][nj] == 'R' or bd[ni][nj] == 'G')) or bd[i][j] == bd[ni][nj]:
                    q2.append((ni, nj))
                    visited2[ni][nj] = 1

N = int(input())
bd = [list(input()) for _ in range(N)]
visited1 = [[0] * N for _ in range(N)]
visited2 = [[0] * N for _ in range(N)]
# print(bd)
cnt1 = 0
cnt2 = 0

for i in range(N):
    for j in range(N):
        if not visited1[i][j]:
            type1(i,j)  # 적록색약이 아닌 사람이 본 구역 수
            cnt1 += 1

for i in range(N):
    for j in range(N):
        if not visited2[i][j]:
            type2(i,j)  # 적록색약이 아닌 사람이 본 구역 수
            cnt2 += 1

print(cnt1, cnt2)