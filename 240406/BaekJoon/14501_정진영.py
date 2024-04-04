"""
접근 : 브루트포스
idea :
모든 경우의 수 탐색
-> N+1 초과할 경우 return
-> N+1에 도착했을 경우 max_value 업데이트

python | pypy
메모리 : 31120KB, 111332KB
시간 : 52ms, 124ms


"""

def dfs(i,p):# 현재 i번째 날 진행한 금액 s, 진행 여부 확인
    global  max_value
    if i>N+1:
        return
    if i == N+1:
        max_value = max(max_value,p)
        return

    dfs(i+T[i],p+P[i]) # i번째 날 상담 진행
    dfs(i+1,p) # 상담 진행 x
N = int(input())
T = [0] # 더미 생성
P = [0]
for _ in range(N):
    t, p = map(int,input().split())
    T.append(t)
    P.append(p)
max_value = 0

dfs(1,0)

print(max_value)