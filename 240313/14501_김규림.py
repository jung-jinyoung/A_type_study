# 구글에 나온 코드를 보고 이해하려 했으나
# 대충 따라가기는 했는데
# 완벽하게 이해는 안된 느낌스

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (n + 1)          # 날짜별로 얻을 수 있는 최대 이익 저장

for i in range(n):          # i = 상담 시작 날짜
    for j in range(i + arr[i][0], n+1):     # j =  상담 끝나는 날짜
        if dp[j] < dp[i] + arr[i][1]:
            dp[j] = dp[i] + arr[i][1]

print(dp[-1])

