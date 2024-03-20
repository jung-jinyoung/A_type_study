"""

메모리 : 116068KB ...
시간 : 444ms (pypy3)
"""

def finding(arr):
    for i in range(R):
        for j in range(C):
            if arr[i][j] == -1:
                machine.append(i)
            if len(machine) == 2:
                return
from collections import deque

R, C, T = map(int,input().split())
# R *C 배열에서 T 초 동안 확인
arr = [list(map(int,input().split())) for _ in range(R)]

# 공기 청정기가 위치한 행 인덱스 저장 리스트
machine = []
finding(arr)


t = 0
while t!=T:

    # 미세 먼지 확산
    # 네방향으로 arr[r][c]//5 만큼 확산

    visited = [[0] * C for _ in range(R)]  # 확산된 먼지 이동 저장
    for i in range(R):
        for j in range(C):
            if arr[i][j] >= 5:

                # 확산될 양
                dust = arr[i][j] // 5
                # 확산된 범위 초기화
                cnt = 0
                for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < R and 0 <= nj < C:
                        # 공기 청정기를 만나면
                        if arr[ni][nj] == -1:
                            continue
                        # 배열을 벗어나지 않을 경우
                        if 0 <= ni < R and 0 <= nj < C:
                            visited[ni][nj] += dust
                            cnt += 1
                # 확산된 만큼 빼주기
                arr[i][j] -= dust * cnt
    # 확산된 먼지 더해주기
    for i in range(R):
        for j in range(C):
            arr[i][j] += visited[i][j]


    # 공기 청정기 작동
    # 공기 청정기가 돌아가는 구역 리스트로 설정
    # rotate -> 다시 하나씩 넣기

    # 공기 청정기 상부
    up=deque()
    dir1 = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    pos1 = [(machine[0],0),(machine[0],C-1),(0,C-1),(0,0)]
    for k in range(4):
        i, j = pos1[k]
        ni = i + dir1[k][0]
        nj = j + dir1[k][1]

        while 0<=ni<machine[1] and 0<=nj<C:
            if arr[ni][nj] == -1:
                up.append(0)
                break
            up.append(arr[ni][nj])
            ni+=dir1[k][0]
            nj+=dir1[k][1]
    up.rotate(1)

    # 공기 청정기 하부
    dn = deque()
    dir2 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    pos2 = [(machine[1], 0), (machine[1], C - 1), (R-1, C - 1), (R-1, 0)]
    for k in range(4):
        i, j = pos2[k]
        ni = i + dir2[k][0]
        nj = j + dir2[k][1]

        while machine[1] <= ni < R and 0 <= nj < C:
            if arr[ni][nj] == -1:
                dn.append(0)
                break
            dn.append(arr[ni][nj])
            ni += dir2[k][0]
            nj += dir2[k][1]
    dn.rotate(1)

    # update
    for k in range(4):

        ux, uy = pos1[k] # 상부 순회 위치
        dx, dy = pos2[k] # 하부 순회 위치

        nux, nuy = ux+dir1[k][0], uy+dir1[k][1] # 상부 순회
        ndx, ndy = dx+dir2[k][0], dy+dir2[k][1] # 하부 순회

        while 0 <= nux < machine[1] and 0 <= nuy < C:
            if arr[nux][nuy] == -1: # 공기 청정기를 만났다면 brake
                break

            arr[nux][nuy] = up.popleft() # update
            nux += dir1[k][0]
            nuy += dir1[k][1]

        while machine[1] <= ndx < R and 0 <= ndy < C:
            if arr[ndx][ndy] == -1: # 공기 청정기를 만났다면 brake
                break
            arr[ndx][ndy] = dn.popleft() # update
            ndx += dir2[k][0]
            ndy += dir2[k][1]

    t+=1 # 시간 증가

total = 0
for i in range(R):
    for j in range(C):
        if arr[i][j]>0: # 먼지가 있으면 저장
            total+=arr[i][j]
print(total)
