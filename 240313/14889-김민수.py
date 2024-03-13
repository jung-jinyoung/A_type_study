"""
축구를 하기 위해 모인 사람은 총 N명
N은 짝수이다.
N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 함
요리사 문제

축구를 재밌게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소
능력치의 차이의 최솟값을 출력
"""
def dfs(n, at, bt):
    global min_v
    # 한 팀이 이미 M명 초과인 경우
    if len(at) > M or len(bt) > M:
        return

    if n == N:
        if len(at) == len(bt):
            asm = bsm = 0
            for i in range(M):
                for j in range(M):
                    asm += arr[at[i]][at[j]]
                    bsm += arr[bt[i]][bt[j]]
            min_v = min(min_v, abs(asm-bsm))
        return

    dfs(n+1, at+[n], bt)    # A팀 선택
    dfs(n+1, at, bt+[n])    # B팀 선택

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
M = N//2
min_v = 100*M
dfs(0, [], [])
print(min_v)