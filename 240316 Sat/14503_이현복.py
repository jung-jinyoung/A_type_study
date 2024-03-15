
'''
14503_로봇청소기
메모리 : 31120KB
시간 : 68ms
'''

N,M =map(int,input().split())
# d => [북,동,남,서] =>시계방향
delta = [(-1,0),(0,1),(1,0),(0,-1)]
r,c,dir = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]    # 0이 청소 안됨, 1은 벽
cnt = 0
while 1:
    if arr[r][c] == 0:
        cnt+=1
        arr[r][c] = 2

    for _ in range(4):
        dir=(dir-1)%4       # 반시계방향이라서 - 해줌
        if arr[r+delta[dir][0]][c+delta[dir][1]] == 0:
            r+=delta[dir][0]
            c+=delta[dir][1]
            break

    else:
        dir+=2      # 뒤로가려고 두칸 작업함
        nx,ny=r+delta[dir%4][0],c+delta[dir%4][1]
        dir+=2
        if arr[nx][ny] != 1:
            r,c=nx,ny
        else: break
print(cnt)
