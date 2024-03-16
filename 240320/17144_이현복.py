import sys
sys.stdin = open('sample_input.txt','r')

'''
17144_미세먼지 안녕!
pypy3 : 115588KB/644ms
python3 :시간초과
'''
def rotate(idx):    # 공기청정기로 돌리는거
    remeber = [new_arr[idx][C-1],new_arr[0][0],new_arr[idx+1][C-1],new_arr[R-1][0]]   # 증발 되는 값 저장용
    for j in range(1,C):                        # 가로 방향 움직임
        new_arr[0][j-1]=new_arr[0][j]                   # 윗줄 움직임(반시계)
        new_arr[idx][C-j]=new_arr[idx][C-j-1]           # 아래줄 움직임(반시계)

        new_arr[R-1][j-1]=new_arr[R-1][j]               # 윗줄 움직임(시계)
        new_arr[idx+1][C-j]=new_arr[idx+1][C-j-1]       # 아래줄 움직임(시계)

    new_arr[idx][1],new_arr[idx+1][1]=0,0

    for i in range(1,idx):                      # 세로 방향 움직임
        new_arr[idx-i][0] = new_arr[idx-i-1][0]   
        new_arr[i-1][C-1] = new_arr[i][C-1]

    for i in range(idx+1,R-1-1):
        new_arr[i+1][0] = new_arr[i+2][0]   
        new_arr[R-i+idx][C-1] = new_arr[R-i+idx-1][C-1]

    new_arr[1][0],new_arr[idx-1][C-1] = remeber[1],remeber[0]
    new_arr[R-1-1][0],new_arr[idx+1+1][C-1] = remeber[3],remeber[2]


R,C,T = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(R)]
for row in range(R):
    if arr[row][0]==-1:
        purifier = row      # 공기청정기 윗부분 좌표 구하기
        break

for _ in range(T):
    new_arr=[[0]*C for _ in range(R)]
    new_arr[purifier][0],new_arr[purifier+1][0]=-1,-1

    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                cnt = 0
                diffusion = [0]*4
                for di,dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                    ni,nj=i+di,j+dj
                    if 0<=ni<R and 0<=nj<C and arr[ni][nj]!=-1:
                        diffusion[cnt]=(ni,nj)                  # 확산 가능한 지점 좌표만 저장해두기
                        cnt+=1
                new_arr[i][j] += (arr[i][j]-arr[i][j]//5*cnt)
                for k in range(cnt):
                    new_arr[diffusion[k][0]][diffusion[k][1]] += arr[i][j]//5
    rotate(purifier)
    arr =new_arr[:][:]

res=0
for i in range(R): res+=sum(arr[i])
print(res+2)



