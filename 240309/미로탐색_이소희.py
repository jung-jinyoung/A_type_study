'''
(1,1) 에서 출발하여 (N,M) 칸으로 가려면 몇 칸을 이동해야 하나
'''
di = [0,1,0,-1]
dj = [1,0,-1,0]
def bfs(i,j):
    q = [[i,j]]
    countarr[i][j] = 0
    while q:
        t = q.pop(0)
        i, j = t[0], t[1]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N+1 and 0<= nj < M+1 and countarr[ni][nj] == 0:
                if maze[ni][nj] == 1:
                    q.append([ni, nj])
                    countarr[ni][nj] = countarr[i][j] + 1
                if maze[ni][nj] == 3:
                    countarr[ni][nj] = countarr[i][j] + 1
                    return countarr[ni][nj] + 1
    return 0

N, M = map(int, input().split())
maze = [[0] * (M+1) ] + [[0] + list(map(int, input())) for _ in range(N)]
maze[N][M] = 3
for m in maze:
    print(m)
countarr = [[0] * (M+1) for _ in range(N+1)]
print(bfs(1,1))

# def route(p, q):
#     stack = []
#     cnt = 0
#     while True:
#         for k in range(4):
#             np = p + dp[k]
#             nq = q + dq[k]
#             if 0 <= np < N and 0 <= nq < M :
#                 if maze[np][nq] == 1: 
#                     stack.append((p,q))
#                     maze[np][nq] = -1
#                     p = np
#                     q = nq
#                     cnt += 1
#                     break
#             if np == N-1 and nq == M-1:
#                 return cnt
#         else:
#             if stack:
#                 p, q = stack.pop()
#             else:
#                 break
