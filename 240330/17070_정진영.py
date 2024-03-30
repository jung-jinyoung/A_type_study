"""
메모리 : 31120KB
시간 : 48ms

"""


N = int(input()) # 집의 크기
room = [list(map(int,input().split())) for _ in range(N)]
# 방의 상태 : 빈 칸은 0, 벽은 1
# (1,1)과  (1,2)는 항상 빈칸 -> 파이프 위치

dp =  [[[0] * 3 for _ in range(N)] for _ in range(N)]  # DP 설정
# 저장 값 : (i,j,k) = > (i,j)위치에서 방향 인덱스 k (가로 0, 세로 1, 대각선 2)
dp[0][1][0] = 1 # 현재 파이프 위치 : (0,1)에서 가로로 놓임

for i in range(N):
    for j in range(2,N):
        if not room[i][j]: # 탐색 위치가 빈 벽이면
            # 이동

            # 가로 방향으로 오는 경우
            dp[i][j][0] = dp[i][j-1][0]+dp[i][j-1][2]

            # 세로 방향으로 오는 경우
            dp[i][j][1] = dp[i-1][j][1]+dp[i-1][j][2]

            # 대각선으로 오는 경우
            if room[i-1][j]==0 and room[i][j-1]==0:
                dp[i][j][2] = dp[i-1][j-1][0]+dp[i-1][j-1][1]+dp[i-1][j-1][2]

print(sum(dp[N-1][N-1]))