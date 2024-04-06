N = int(input()) # 며칠 후에 퇴사하는지
info = []
for _ in range(N):
    day, pay = map(int, input().split())
    info.append((day, pay))
maxearn = 0

def dfs(i, earn):
    global maxearn
    if i >= N:
        maxearn = max(maxearn, earn)
        return
    if i + info[i][0] <= N:
        dfs(i + info[i][0], earn + info[i][1])
    dfs(i+1, earn)

dfs(0,0)
print(maxearn)