"""
두번째 테스트 케이스에서 fail...
"""


# 구름 이동 함수
def move(d,s,clouds):
    moved_clouds = []
    for cloud in clouds:
        x, y = cloud
        nx = (x + di[d][0]*s) % N
        ny = (y + di[d][1]*s) % N
        moved_clouds.append((nx,ny))
    return moved_clouds


# 비내리기 함수
def water_magic(clouds):
    for cloud in clouds :
        x,y = cloud
        square[x][y] += 1

#물 복사 버그 함수
def copy_water(clouds):
    for cloud in clouds:
        x,y = cloud
        cnt = 0
        for i in [2,4,6,8]:
            nx = x+di[i][0]
            ny = y+di[i][1]
            # 범위에서 벗어나지 않고 바구니가 있다면
            if 0<=nx<N and 0<=ny<N and square[nx][ny]>0:
                 cnt+=1

        #물 복사 버그 : 바구니 개수 만큼 증가
        square[x][y]+=cnt

# 새로운 구름 생성 함수
def new_clouds():
    new_clouds = []
    for i in range(N):
        for j in range(N):
            if (i,j) not in clouds and square[i][j]>=2:
                new_clouds.append((i,j))
                square[i][j] -=2
    return new_clouds

# 모든 바구니의 물의 양 합 구하기
def sum_water():
    global result
    for i in range(N):
        for j in range(N):
            result += square[i][j]



N, M = map(int, input().split())
# 더미 생성, di 인덱스 별 이동 방향 설정
di = [(0),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(0,1),(1,-1)]
square = [list(map(int, input().split())) for _ in range(N)]

# 현재 구름 위치
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
for _ in range(M):
    # 구름 이동
    d, s = map(int,input().split())
    clouds = move(d,s,clouds)
    # 비 내리기
    water_magic(clouds)
    # 대각선으로 물 복사 버그
    copy_water(clouds)

    # 물의 양이 2 이상인 칸에 구름 생성
    clouds = new_clouds()

result = 0
sum_water()
print(result)