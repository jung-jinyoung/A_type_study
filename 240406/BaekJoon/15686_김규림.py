def func(house, chickens):      # 해당 치킨집과 집 거리 구하기
    total = 0
    for hx, hy in house:
        ans = float('inf')
        for cx, cy in chickens:
            dist = abs(hx - cx) + abs(hy - cy)
            ans = min(ans, dist)
        total += ans
    return total


def dfs(idx, select, chicken):
    global result
    if len(select) == M:  # M개의 치킨집 선택한 경우
        result = min(result, func(house, select))
        return

    if idx == len(chicken):  # 모든 치킨집을 검사한 경우
        return

    # 해당 치킨집 선택하는 경우
    dfs(idx + 1, select + [chicken[idx]], chicken)
    # 해당 치킨집 선택하지 않는 경우
    dfs(idx + 1, select, chicken)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 집과 치킨집 위치 파악
house = []
chicken = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append((i, j))
        elif arr[i][j] == 2:
            chicken.append((i, j))

result = float('inf')
dfs(0, [], chicken)  # DFS를 통해 모든 조합 탐색

print(result)
