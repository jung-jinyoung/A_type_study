def dfs(k, pay):
    global ans
    if k >= N:
        ans = max(ans, pay)
        return
    if k + arr[k][0] <= N:
        dfs(k + arr[k][0], pay + arr[k][1])
    dfs(k+1, pay)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
dfs(0,0)
print(ans)
