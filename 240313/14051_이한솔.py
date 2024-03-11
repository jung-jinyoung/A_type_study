# 퇴사

N = int(input()) # 퇴사까지 남은 날
T = []
P = []
dp = [0]*(N+1)
max_v = 0

for _ in range(N):
    x, y = map(int, input().split())
    T.append(x)
    P.append(y)

for i in range(N-1,-1,-1):
    time = T[i] + i
    if time <= N:
        dp[i] = max(P[i] + dp[time], max_v)
        max_v = dp[i]
    else:
        dp[i] = max_v
print(max_v)

        