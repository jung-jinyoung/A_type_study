'''
시간 2520 ms / 메모리 31120 KB
'''
# 확산
def spread():
    after = [[0] * c for _ in range(r)]  # 확산 이후 미세먼지 임시 저장
    for i in range(r):
        for j in range(c):
            if room[i][j] > 0:  # 미세먼지가 있는 경우에
                amount = room[i][j] // 5
                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < r and 0 <= nj < c and room[ni][nj] != -1:
                        after[ni][nj] += amount
                        room[i][j] -= amount
    # 확산이 끝나고 원래 배열에 추가
    for i in range(r):
        for j in range(c):
            room[i][j] += after[i][j]

def clean():
    # 위쪽 공기청정기 작동
    for i in range(cleaner[0]-1, 0, -1):
        room[i][0] = room[i-1][0]
    for j in range(c-1):
        room[0][j] = room[0][j+1]
    for i in range(cleaner[0]):
        room[i][-1] = room[i+1][-1]
    for j in range(c-1, 1, -1):
        room[cleaner[0]][j] = room[cleaner[0]][j-1]
    room[cleaner[0]][1] = 0   # 청정기에서 나온 공기

    # 아래쪽 공기청정기 작동
    for i in range(cleaner[1]+1, r-1):
        room[i][0] = room[i+1][0]
    for j in range(c-1):
        room[-1][j] = room[-1][j+1]
    for i in range(r-1, cleaner[1], -1):
        room[i][-1] = room[i-1][-1]
    for j in range(c-1, 1, -1):
        room[cleaner[1]][j] = room[cleaner[1]][j-1]
    room[cleaner[1]][1] = 0   # 청정기에서 나온 공기

r, c, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]
cleaner = []
for i in range(r):
    if room[i][0] == -1:
        cleaner.append(i)
        cleaner.append(i+1)
        break
# t번 반복
for _ in range(t):
    spread()
    clean()

# 남은 미세먼지 양 계산
dust_sum = 0
for i in range(r):
    for j in range(c):
        if room[i][j] > 0:
            dust_sum += room[i][j]
print(dust_sum)
