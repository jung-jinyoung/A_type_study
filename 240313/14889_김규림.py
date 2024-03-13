N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [0] * N
min_num = float('inf')      # 양의 무한대


def func(D, idx):           # 깊이, 인덱스
    global min_num
    if D == N // 2:         # 선수 중, 절반을 돌았다면 (나머지 반은 다른 팀)
        A = 0
        B = 0
        for i in range(N):
            for j in range(N):
                if visited[i] == 1 and visited[j] == 1:
                    A += arr[i][j]
                elif visited[i] == 0 and visited[j] == 0:
                    B += arr[i][j]
        min_num = min(min_num, abs(A-B))
        return

    # D가 N // 2 가 아니라면,
    for k in range(idx, N):     # idx부터 돌기. 전에 확인했던 선수들 다시 확인 안하려고
        if visited[k] == 0:     # 확인 안 한 선수면
            visited[k] = 1      # 확인
            func(D+1, k+1)      # 재귀 호출
            visited[k] = 0      # 원상 복구


func(0,0)
print(min_num)
