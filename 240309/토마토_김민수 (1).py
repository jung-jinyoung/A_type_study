"""
토마토는 한칸씩 넣어서 보관
익지 않은 토마토들도 있을 수 있다
보관 후 하루가 지나면 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 
토마토의 영향을 받아 익게 됨.

인접은 상하좌우

토마토가 저절로 익는 경우는 없다.

며칠이 지나면 다 익게 되는지 최소 일수를 구하라

단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있음

1은 익은 토마토
0은 익지 않은 토마토
-1은 토마토가 들어있지 않은 칸

저장될 때 부터 모든 토마토가 익어있는 상태이면 0을 출력

토마토가 모두 익지는 못하는 상황이면 -1 출력
"""
from collections import deque
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
d = deque()

for i in range(M):
    for j in range(N):
        if arr[i][j] == 1:      # 토마토 발견 했을때
            d.append((i, j))    # 토마토 좌표 push

while d:
    k, l = d.popleft()
    for di, dj in [[0,1], [1,0], [-1,0], [0,-1]]:
        ni, nj = k+di, l+dj
        if 0<=ni<M and 0<=nj<N and arr[ni][nj] == 0:
            arr[ni][nj] = arr[k][l] + 1
            d.append((ni, nj))

result = 0
for p in arr:
    if 0 in p:
        result = 0
        break
    else:
        result = max(result, max(p))

print(result-1)     # 토마토가 0으로 시작하기 때문에 -1을 해줘야 날짜로 변환 가능