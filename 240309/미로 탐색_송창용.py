# 2178_bj(미로 탐색)
'''
https://www.acmicpc.net/problem/2178
'''
def bfs(start):
    q = [start]
    while q:
        x, y = q.pop(0)
        for d in [0, 1], [0, -1], [1, 0], [-1, 0]:
            mx = x + d[0]
            my = y + d[1]
            if 0 <= mx < m and 0 <= my < n:
                if visited[my][mx] == 0 and maze[my][mx] == 1:
                    q.append([mx, my])
                    visited[my][mx] = visited[y][x] + 1

n, m = map(int, input().split())
maze = []
visited = [[0] * m for _ in range(n)]
visited[0][0] = 1

for _ in range(n):
    maze.append(list(map(int, input())))

bfs([0, 0])
print(visited[n-1][m-1])