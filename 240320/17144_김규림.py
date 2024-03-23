def clean(pos):
    # 반시계 방향
    for p in range(pos-1, 0, -1):       # 공기청정기 위쪽부터 0까지
        arr[p][0] = arr[p-1][0]         # 먼지 아래로 이동/ 열의 값
    arr[0][:-1] = arr[0][1:]            # 먼지 왼쪽으로 이동

    for p in range(pos):
        arr[p][-1] = arr[p+1][-1]       # 먼지 위로 이동
    arr[pos][2:] = arr[pos][1:-1]       # 먼지 오른쪽으로 이동
    arr[pos][1] = 0                     # 공기청정기 위치의 두번째 열은 0

    pos += 1        # 공기청정기 다음 행으로 이동

    # 시계 방향
    for q in range(pos+1, len(arr)-1):  # 공청 위치 ~ 아래쪽 탐색
        arr[q][0] = arr[q+1][0]         # 아래에서 위로 이동
    arr[-1][:-1] = arr[-1][1:]          # 왼쪽 이동

    for q in range(len(arr)-1, pos, -1):    # 배열 마지막 행부터 공청 있는데까지
        arr[q][-1] = arr[q-1][-1]       # 아래로 이동
    arr[pos][2:] = arr[pos][1:-1]       # 오른쪽 이동
    arr[pos][1] = 0


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

r, c, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]

pos = 0
# 공기청정기 위치 확인
for i in range(r):
    if arr[i][0] == -1:
        pos = i
        break

for _ in range(t):
    brr = [[0 for _ in range(c)] for _ in range(r)]

    # 미세먼지 이동
    for x in range(r):
        for y in range(c):
            if arr[x][y] >= 5:
                for k in range(4):
                    ni = x + di[k]
                    nj = y + dj[k]
                    if 0 <= ni < r and 0 <= nj < c and arr[ni][nj] != -1:
                        brr[ni][nj] += arr[x][y] // 5
                        brr[x][y] -= arr[x][y] // 5

    # 이동한 미세먼지 반영
    for a in range(r):
        for b in range(c):
            arr[a][b] += brr[a][b]

    # 공기청정기 작동
    clean(pos)

# 미세먼지 양 출력
total = 0
for rr in range(r):
    total += sum(arr[rr])

# 공기청정기가 -1로 표시되어있으므로
print(total + 2)



