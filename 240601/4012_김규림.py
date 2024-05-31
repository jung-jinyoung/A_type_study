def dfs(n, alst, blst):
    global ans
    if n == N:                      # 모든 재료를 선택했을 경우
        if len(alst) == N // 2:     # a 음식에 선택된 재료 개수가 절반일 경우
            asum = 0                # 음식 맛의 합 구하기
            bsum = 0
            for i in range(N//2):
                for j in range(N//2):
                    asum += arr[alst[i]][alst[j]]       # a 음식 맛 더하기
                    bsum += arr[blst[i]][blst[j]]       # b 음식 맛 더하기

            ans = min(ans, abs(asum-bsum))      # 최소 맛 차이
        return

    dfs(n+1, alst+[n], blst)              # a 음식에 추가하고 재귀 호출
    dfs(n+1, alst, blst+[n])              # b 음식에 추가하고 재귀 호출


T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 20000 * N * N

    dfs(0, [], [])            # dfs(n, alst, blst)

    print(f'#{t+1} {ans}')

