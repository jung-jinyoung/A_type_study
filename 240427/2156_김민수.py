"""
포도주 잔이 일렬로 놓여있음
1. 포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야함
2. 연속으로 놓여 있는 3잔을 모두 마실 수는 없음

1부터 n까지 순서대로 번호가 붙어져있음
될 수 있는 대로 많은 양의 포도주를 마셔야 함

양이 많은 순서 대로 집고 만약 연속으로 해당하는 인덱스는 제외
"""
# 리커젼 에러
def dfs(index, count, total):
    global max_total

    if count >= 3:  # 연속으로 3잔을 마신 경우
        return

    if index >= N-1:  # 마지막 포도주까지 고려했을 때
        max_total = max(max_total, total)
        return

    # 현재 포도주를 마시는 경우
    dfs(index + 1, count + 1, total + wines[index])
    # 현재 포도주를 마시지 않는 경우
    dfs(index + 1, 0, total)


N = int(input())
wines = [int(input()) for _ in range(N)]  # [6, 10, 13, 9, 8, 1]
max_total = 0
dfs(0, 0, 0)
print(max_total)

########################################################

N = int(input())

# 포도주 잔의 양을 리스트에 저장합니다.
wines = [int(input()) for _ in range(N)]

# 최대로 마실 수 있는 포도주 양을 계산하는 함수입니다.
def max_wine(n, wines):
    # 동적 계획법을 사용하기 위한 배열을 초기화합니다.
    dp = [0] * (n + 1)

    # 첫 번째 잔의 경우를 처리합니다.
    dp[1] = wines[0]

    # 두 번째 잔의 경우를 처리합니다.
    if n >= 2:
        dp[2] = wines[0] + wines[1]

    # 세 번째 잔부터는 두 가지 경우를 고려하여 최대값을 선택합니다.
    for i in range(3, n + 1):
        # 현재 잔을 마시지 않는 경우와 현재 잔을 마시는 경우를 고려하여 최대값을 계산합니다.
        # 현재 잔을 마시는 경우에는 i-1번째 잔을 마시지 않은 경우, i-2번째 잔을 마시지 않은 경우, i-3번째 잔까지 마신 경우의 합 중 최대값을 선택합니다.
        dp[i] = max(dp[i - 1],            # 현재 잔을 마시지 않는 경우
                    dp[i - 2] + wines[i - 1],     # 현재 잔을 마시고 이전 잔을 마시지 않는 경우
                    dp[i - 3] + wines[i - 2] + wines[i - 1])   # 현재 잔을 마시고 이전 두 잔을 마신 경우

    # 마지막 잔까지 고려한 최대 포도주 양을 반환합니다.
    return dp[n]

# 최대 포도주 양을 출력합니다.
print(max_wine(N, wines))

"""
① 현재 포도주와 이전 포도주를 마시고 전전 포두주는 마시지 않는다. ( wine[i]+wine[i-1]+d[i-3] )

② 현재 포도주와 전전 포도주를 마시고 이전 포도주는 마시지 않는다. ( wine[i]+d[i-2] )

③ 현재 포도주를 마시지 않는다. ( d[i-1] )

 

이 세 가지 경우로 나눌 수 있다.

이 때, 3번케이스의 경우 d[i-2]+wine[i-1] 로 표기하지 않은 이유는

d[i-1]에 해당 케이스를 포함한 최댓값이 저장되어 있기 때문이다.
"""

n = int(input())

wine = []

for i in range(n):
    wine.append(int(input()))

d = [0]*n

d[0] = wine[0]
if n > 1:
    d[1] = wine[0]+wine[1]

if n > 2:
    d[2] = max(wine[2]+wine[1], wine[2]+wine[0], d[1])

for i in range(3, n):
    d[i] = max(d[i-1], d[i-3]+wine[i-1]+wine[i], d[i-2]+wine[i])

print(d[n-1])