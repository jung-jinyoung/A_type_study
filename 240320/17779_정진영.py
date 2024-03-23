"""
인덱스 에러 계속 발생 ㅠㅠ

"""

def check(x, y, d1, d2):
    # 선거구 경계 설정
    graph = [[0] * N+1 for _ in range(N+1)]


    for i in range(d1 + 1):
        graph[x + i][y - i] = 5
        graph[x + d2 + i][y + d2 - i] = 5
    for i in range(d2 + 1):
        graph[x + i][y + i] = 5
        graph[x + d1 + i][y - d1 + i] = 5
    print(*graph,sep = '\n')

    # 1번 ~ 4번 선거구 설정
    districts = [0] * 5
    for r in range(1,N+1):
        for c in range(1,N+1):
            if graph[r][c] == 5:
                districts[4] += population[r][c]
            elif r < x + d1 and c <= y and graph[r][c] != 5:
                districts[0] += population[r][c]
            elif r <= x + d2 and y < c <= N - 1 and graph[r][c] != 5:
                districts[1] += population[r][c]
            elif x + d1 <= r <= N - 1 and c < y - d1 + d2 and graph[r][c] != 5:
                districts[2] += population[r][c]
            elif x + d2 < r <= N - 1 and y - d1 + d2 <= c <= N - 1 and graph[r][c] != 5:
                districts[3] += population[r][c]

    # 선거구 인구 수의 최솟값과 최댓값 반환
    return min(districts), max(districts)


N = int(input())
population = [0] + [list(map(int, input().split())) for _ in range(N)]

ans = int(1e9)
for x in range(1,N):
    for y in range(1,N):
        for d1 in range(1, N):
            for d2 in range(1, N):
                if x + d1 + d2 <= N and 1 <= y - d1 and y + d2 <= N:
                    min_tmp, max_tmp = check(x, y, d1, d2)
                    ans = min(ans, max_tmp - min_tmp)

print(ans)
