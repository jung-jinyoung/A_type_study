# 7576_bj(토마토)
'''
https://www.acmicpc.net/problem/7576
'''
import sys
from collections import deque

m, n = map(int, input().split())
tomato = []
start = deque()
result = 0
flag = False

for y in range(n):
    tomato.append(list(map(int, sys.stdin.readline().split())))
    for x in range(m):
        if tomato[y][x] == 1:
            start.append((x, y))

while start:
    x, y = start.popleft()
    for d in [0, 1], [0, -1], [1, 0], [-1, 0]:
        mx = x + d[0]
        my = y + d[1]
        if 0 <= mx < m and 0 <= my < n and tomato[my][mx] == 0:
            start.append((mx, my))
            tomato[my][mx] = tomato[y][x] + 1

for t in tomato:
    if 0 in t:
        print(-1)
        exit()
    else:
        result = max(result, max(t))

print(result - 1)