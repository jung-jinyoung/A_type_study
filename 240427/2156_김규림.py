N = int(input())
wine = [0] + [int(input()) for _ in range(N)]

dp = [0] * (N+1)
dp[1] = wine[1]
if N > 1:
    # 첫번째, 두번째 와인 잔을 선택했을 때, 최대 양
    dp[2] = wine[1] + wine[2]

# 세번째 와인 잔부터 돌면서 각 와인잔 선택했을 때 최대 양 구해줌
for i in range(3, N+1):
    dp[i] = max(dp[i-2]+wine[i], dp[i-1], dp[i-3]+wine[i-1]+wine[i])
    # 현재 와인 잔 선택 X: dp[i-1]
    # 현재 와인 잔 선택 O : dp[i-2]+wine[i]
    # 현재 와인 잔 + 이전에 선택한 와인 잔과 함께 마심: dp[i-3]+wine[i-1]+wine[i]

print(dp[N])
