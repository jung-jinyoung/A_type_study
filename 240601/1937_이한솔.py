'''
욕심쟁이 푸바오

n * n 대나무 숲
한 지점에서 대나무를 먹기 시작 -> 상 하 좌 우 중 한 곳으로 이동
단, 전에 있던 대나무의 양보다 많아야함
최대한 많은 칸을 이동할 수 있도록

DFS
DP
'''

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x,y):
    if visited[x][y]: # 이미 지나온 경로일 경우 해당 지점의 값부터 시작
        return visited[x][y]
    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n and graph[x][y] < graph[nx][ny]:
            visited[x][y] = max(visited[x][y], dfs(nx, ny) + 1) 
    return visited[x][y]

n = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)] # 해당 위치에서 이동할 수 있는 칸의 개수를 저장

go = 0
for i in range(n):
    for j in range(n):
        go = max(go, dfs(i,j))

print(go)
