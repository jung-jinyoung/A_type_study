"""
반시계 방향으로 이동
d는 현재 로봇 청소기가 바라보는 방향

주변에 청소할 구역이 없다면 후진
청소할 구역이 있을 경우 해당 구역으로 이동

시간 : 40ms
메모리 31120KB

"""

N , M = map(int,input().split())
#현재 로봇 청소기가 있는 칸의 좌표
r, c ,d = map(int,input().split())
#현재 방의 상태
room = [list(map(int,input().split())) for _ in range(N)]

# 북쪽 0 동쪽 1 남쪽 2 서쪽 3
# 반 시계 방향으로 이동하기 위한 방향 리스트
direction =[1,2,3,0]
di = [-1,0,1,0]
dj = [0,1,0,-1]

cnt = 0 # 청소한 구역 카운트
visited= [[0]*M for _ in range(N)]


#현재 구역 청소
cnt +=1
visited[r][c]=1


while True :
    check = 0

    for _ in range(4):
        # 반 시계 방향으로 회전
        d = (d+3)%4
        ni = r+di[d]
        nj = c+dj[d]

        if (0 <= ni < N and 0 <= nj < M) and not room[ni][nj]:
            if not visited[ni][nj]:
                visited[ni][nj] = 1
                cnt += 1
                check = 1
                r = ni
                c = nj
                break


    if check == 0 :
        if room[r-di[d]][c-dj[d]] == 1:
            print(cnt)
            break
        else:
            r, c = r-di[d], c-dj[d]



