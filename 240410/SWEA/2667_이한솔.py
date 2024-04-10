# 단지 번호 붙이기

'''
N : 지도의 크기
visited 배열 필요
배열 순회하면서 방문하지 않은 1을 만나면 함수 호출
'''
di = [0,1,0,-1]
dj = [1,0,-1,0]
def bfs(si,sj):
    q = []
    q.append((si,sj))
    visited[si][sj] = 1
    cnt = 1

    while q:
        ci,cj = q.pop(0)
        for n in range(4):
            mi = ci+di[n]
            mj = cj+dj[n]
            if 0<=mi<N and 0<=mj<N and visited[mi][mj] == 0 and apart[mi][mj] == 1:
                q.append((mi,mj))
                visited[mi][mj] = 1
                cnt += 1
                
    return cnt

N = int(input())
apart = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
ans = []

for i in range(N):
    for j in range(N):
        if apart[i][j] == 1 and visited[i][j] == 0:
            ans.append(bfs(i,j))

ans.sort()
print(len(ans), *ans, sep='\n')
