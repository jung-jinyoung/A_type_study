# 2667_bj(단지번호붙이기)
'''
https://www.acmicpc.net/problem/2667
'''
def bfs(start):
    global cnt
    c = 1
    q = [start]
    house[start[1]][start[0]] = 0
    while q:
        x, y = q.pop(0)
        for d in [1, 0], [-1, 0], [0, 1], [0, -1]:
            mx = x + d[0]
            my = y + d[1]
            if 0 <= mx < n and 0 <= my < n and house[my][mx] == 1:
                house[my][mx] = 0
                q.append([mx, my])
                c += 1
    cnt += 1
    result.append(c)

n = int(input())
house = [list(map(int, input())) for _ in range(n)]
cnt = 0
result = []

for y in range(n):
    for x in range(n):
        if house[y][x] == 1:
            bfs([x, y])

result.sort()
print(cnt)
print(*result, sep='\n')