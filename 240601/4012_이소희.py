# 백트래킹
def dfs(k, aList, bList):
    global answer
    if k == N :
        if len(aList) == M:
            aSum = bSum = 0
            for i in range(M):
                for j in range(M):
                    aSum += arr[aList[i]][aList[j]]
                    bSum += arr[bList[i]][bList[j]]
            answer = min(answer, abs(aSum - bSum))
        return

    dfs(k+1, aList + [k], bList)
    dfs(k+1, aList, bList + [k])
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M =  N // 2
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 10 ** 5 * N

    # dfs(시작점, aList, bList)
    dfs(0, [], [])

    print(f'#{tc} {answer}')