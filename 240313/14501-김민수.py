"""
오늘부터 N+1일째 되는 날 퇴사를 하기위해
남은 N일 동안 최대한 많은 상담

하루에 하나씩 서로 다른 사람의 상담

각각의 상담을 완료하는데 걸리는 기간 T와 상담을 했을 때 받을 수 있는 금액 P
"""
# N = int(input())
# arr = [0] + [list(map(int, input().split())) for _ in range(N)]
#
# max_v = 0       # 최대 이익
#
# for i in range(1, N+1):     # 1일부터 N일까지
#     money = 0               # 각 상담을 진행했을때 최종적으로 번 돈
#     for j in range(i+1, N+1):   # 시작 이후 날
#         if arr[i][0] <= N-i:    # N일중 arr[i][0]에 해당하는 날이 남아있는 날보다 작을 때만 가능
#             money += arr[i][1]  # 상담 시작점 더하기

N = int(input())
T = [0]*N
P = [0]*N
for i in range(N):
    T[i], P[i] = map(int, input().split())

dp = [0]*(N+1)
for n in range(N-1, -1, -1):    # 뒤에서 앞으로 (완료기준)
    if n+T[n] <= N:             # 기간내 상담 완료 가능
        dp[n] = max(dp[n+1], dp[n+T[n]] + P[n])
    else:
        dp[n] = dp[n+1]
print(dp[0])




