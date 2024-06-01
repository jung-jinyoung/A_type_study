'''
백준
1937. 욕심쟁이 판다

n*n 크기의 대나무숲
욕심쟁이 판다는 어떤 지역에서 대나무를 먹기 시작
판다는 대나무를 먹고 자리를 옮기면 옮긴 지역에 그 전 지역보다 대나무가 많이 있어야 한다.

어떤 지점에 풀어 놓아야 하는지?
어떤 경로로 이동하면 최대한 많은 칸을 이동할 수 있는지

첫째 줄에 대나무 숲의 크기 n (1 <= <= 500)
둘째 줄부터 n+1번째 줄까지 대나무 숲의 정보
대나무의 양은 1,000,000보다 작거나 같은 자연수
'''


'''def greedy_panda(y, x, count):
    global max_move

    visited[y][x] = 1
    for di, dj in [1, 0], [0, 1], [-1, 0], [0, -1]:
        ni = y+di
        nj = x+dj
        if 0<=ni<n and 0<=nj<n and not visited[ni][nj] and bamboo[ni][nj] > bamboo[y][x]:
            greedy_panda(ni, nj, count+1)
    if max_move < count:
        max_move = count


n = int(input())
bamboo = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
max_move = 0
while min(map(min, bamboo)) != 1000001:
    break_point = 0
    for i in range(n):
        if break_point:
            break
        for j in range(n):
            if visited[i][j]:
                bamboo[i][j] = 1000001
            if bamboo[i][j] == min(map(min, bamboo)):
                greedy_panda(i, j, 1)
                break_point = 1
                break

print(max_move)'''


def greedy_panda(y, x, count):
    for di, dj in [1, 0], [0, 1], [-1, 0], [0, -1]:
        ni = y+di
        nj = x+dj
        if 0<=ni<n and 0<=nj<n and bamboo[ni][nj] > bamboo[y][x]:
            if visited[ni][nj]:
                if count <= visited[ni][nj]:
                    visited[y][x] = visited[ni][nj]+1
            else:
                greedy_panda(ni, nj, count+1)
                if visited[ni][nj] < dfs_count:
                    visited[ni][nj] = dfs_count


n = int(input())
bamboo = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
max_move = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            greedy_panda(i, j, 1)

print(max(map(max, visited)))

