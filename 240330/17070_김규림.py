def dfs(x, y, dir):
    global result
    if x == N-1 and y == N-1:       # 파이프가 목표지점에 도달했다면
        result += 1                 # result +1
        return

    # 0 = 가로 방향, 1 = 세로 방향, 2 = 대각선 방향
    if x + 1 < N and y + 1 < N:     # 대각선 이동
        if arr[x+1][y+1] == 0 and arr[x][y+1] == 0 and arr[x+1][y] == 0:
            dfs(x+1, y+1, 2)

    if dir == 0 or dir == 2:         # 오른쪽 이동
        if y + 1 < N and arr[x][y+1] == 0:
            dfs(x, y+1, 0)

    if dir == 1 or dir == 2:        # 아래쪽 이동
        if x+1 < N and arr[x+1][y] == 0:
            dfs(x+1, y, 1)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0
dfs(0, 1, 0)      # 이동 전 위치, 방향
print(result)