def dfs(a, b, K, p, l, c):
    global max_length
    max_length = max(l, max_length)

    for d in range(4):
        na = a + di[d]
        nb = b + dj[d]
        if 0 < na <= N and 0 < nb <= N:
            # 현재 위치보다 낮고, 방문하지 않았다면
            if arr[na][nb] < c and visited[na][nb] == 0:
                visited[na][nb] = 1
                dfs(na, nb, K, p, l+1, arr[na][nb])     # l+1 길이 증가
                visited[na][nb] = 0
            # 높이가 현재 위치와 같거나 높고, 공사를 하지 않았다면,
            elif visited[na][nb] == 0 and arr[na][nb] >= c and p == 0:
                # 최대 공사 가능 높이보다 차이가 작다면
                if K > arr[na][nb] - c:
                    visited[na][nb] = 1
                    dfs(na, nb, K, 1, l+1, c-1)
                    visited[na][nb] = 0

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    arr = [[0 for _ in range(N+1)]]
    for _ in range(N):
        brr = list(map(int, input().split()))
        arr.append([0] + brr)

    max_points = []
    max_num = 0
    # 최대 높이 구하기
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] > max_num:
                max_num = arr[i][j]
                max_points = [(i, j)]
            elif arr[i][j] == max_num:
                max_points.append((i, j))

    max_length = 1
    for a, b in max_points:
        visited = [[0] * (N+1) for _ in range(N+1)]
        visited[a][b] = 1
        # a, b = 시작점 , K= 최대 공사 가능 높이, 0 = 공사 여부, 1 = 길이
        dfs(a, b, K, 0, 1, arr[a][b])

    print(f'#{t+1} {max_length}')
