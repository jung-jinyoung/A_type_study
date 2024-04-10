"""
N*N개의 벌통이 정사각형 모양으로 배치
각 칸의 숫자는 벌통에 있는 꿀의 양

각각의 일꾼은 가로로 연속되도록 M개의 벌통을 선택하고, 선택한 벌통에서 꿀을 채취 가능
단 서로 겹치면 안됨.

서로 다른 벌통에서 채취한 꿀이 섞이면 안됨. 따라서 하나의 벌통에서 채취한 꿀은 하나의 용기에 담음
한번 채취한 꿀은 벌통에 있는 모든 꿀을 한번에 채취함.
두 일꾼이 채취할 수 있는 꿀의 최대 양은 C.

벌통 크기 = N, 선택할 수 있는 벌통의 개수 = M, 채취 가능한 최대 꿀의 양 = C
"""
import sys
sys.stdin = open('input.txt')

def dfs(cnt, worker, total, i, j):
    global max_v
    if worker > C:  # 일꾼이 수확한 꿀이 C를 넘어가면 return
        return
    if cnt == M:    # 종료 조건
        max_v = max(total, max_v)
        return

    # 재귀 호출
    # 꿀을 넣었을 경우
    dfs(cnt+1, worker+honey_map[i][j+cnt], total+(honey_map[i][j+cnt])**2, i, j)
    # 안 넣었을 경우
    dfs(cnt+1, worker, total, i, j)



T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())     # 벌통 크기, 인당 벌통 수, 인당 꿀 채취 최대양
    honey_map = [list(map(int, input().split())) for _ in range(N)]

    ans, worker1 = 0, 0
    for i in range(N):
        for j in range(N-M+1):
            max_v = 0
            dfs(0, 0, 0, i, j)  # (i,j) 에서의 일꾼 1의 최대값 구해주기
            worker1 = max_v     # 일꾼1의 최대값 저장
            for k in range(i, N):
                nj = j + M if i == k else 0     # 같은 행인지 아닌지
                for l in range(nj, N-M+1):
                    max_v = 0   # 앞에서 사용했기 때문에 초기화. 일꾼2의 최대값 저장
                    dfs(0, 0, 0, k, l)  # 2번째 일꾼
                    ans = max(ans, worker1+max_v)

    print(f'#{tc} {ans}')