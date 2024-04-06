'''
메모리 71540 KB, 실행시간 205 ms, 코드길이 1186
'''

from collections import deque
# 상 (-1,0) 하 (1,0) 좌 (0,-1) 우 (0,1)
poss = {
    1 : ((-1,0),(1,0),(0,-1),(0,1)),
    2 : ((-1,0),(1,0)),
    3 : ((0,-1),(0,1)),
    4 : ((-1,0),(0,1)),
    5 : ((1,0),(0,1)),
    6 : ((1,0),(0,-1)),
    7 : ((0,-1),(-1,0)),
}

# L이랑 상관없이 배열을 모두 채울 것임.
def bfs(i, j):
    q = deque()
    q.append((i,j))
    visited[R][C] = 1 # 시작점 방문 처리
    while q :
        i, j = q.popleft()
        # 주어진 파이프에서 갈 수 있는 방향만 di, dj로 설정
        for di, dj in poss[mapp[i][j]]:
            ni, nj = i + di, j + dj
            # ni, nj가 범위 내에 있고, 파이프가 있고, 아직 방문한 적이 없으면
            if 0 <= ni < N and 0 <= nj < M and mapp[ni][nj] and visited[ni][nj] == 0:
                # 양쪽이 모두 이어져 있어야 이동가능임
                # 그래서 반대에서도 올 수 있는지 확인을 해야 함
                for dii, djj in poss[mapp[ni][nj]] :
                    nii , njj = ni + dii, nj + djj
                    # 만약에 반대에서도 올 수 있다면, 그건 탈주범의 이동경로가 될 수 있음
                    if (nii, njj) == (i, j):
                        # 그 때 q에 넣고 방문처리
                        q.append((ni, nj))
                        visited[ni][nj] = visited[i][j] + 1

T = int(input())
for tc in range(1, T+1):
    N, M , R, C, L = map(int, input().split())
    mapp = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    bfs(R, C)

    # 그리고 여기서 L이하인 지점만 카운트하기
    cnt = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] and visited[i][j] <= L:
                cnt += 1
    print(f'#{tc} {cnt}')
