"""
접근 : 브루트 포스
idea :
모든 경우의 수 (조합) : 스타트 팀만 구하기 (나머지 자동 링크 팀 )->
각 팀별 능력치의 합 구해서 빼기 ->
min_value 업데이트


python | pypy
메모리 : 31120 KB, 115204 KB
시간 : 5604 ms, 1004 ms


"""
def start_check(i,s): # 현재 i번째 팀원 탐색, 현재 스타트 팀 멤버 인덱스
    global min_value
    if len(s) > M or i >=N:# 스타트팀 결정 or 모든 멤버들을 탐색
        return

    if len(s) == M :
        # 스타트 팀 능력치의 합 구하기
        total_s = 0
        # 멤버별 능력치 합 구하기
        for i in s :
            for j in range(N):
                if j in s and j != i:
                    total_s += info[i][j]

        # 링크 팀 능력치의 합 구하기
        # 링크 팀 멤버 인덱스 구하기
        l = [i for i in range(N) if i not in s]
        total_l = 0

        for i in l:
            for j in range(N):
                if j in l and j != i:
                    total_l += info[i][j]

        result = abs(total_s - total_l)
        min_value = min(min_value, result)
        return

    start_check(i+1, s+[i]) # i번째 멤버 스타트 팀 참가
    start_check(i+1,s) # i번째 멤버 링크 팀 참가



N = int(input())
M = N//2
info = [list(map(int, input().split())) for _ in range(N)]

min_value = int(1e9)

start_check(0,[])

print(min_value)


