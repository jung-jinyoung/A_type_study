import sys
sys.stdin=open('sample_input.txt','r')

'''
 swea_2382_미생물 격리
 메모리 : 85,376 kb
 실행 시간 : 2,386 ms
'''

def move_func(array):
    temp_array = [[0] * N for _ in range(N)]
    temp = []
    for i in range(N):
        for j in range(N):
            if array[i][j]:
                ni,nj=i+delta[array[i][j][1][0]][0],j+delta[array[i][j][1][0]][1]   # 이동 방향으로 이동하기 위한 새 죄표
                if temp_array[ni][nj]==0:                           # 도착 한 곳이 비어 있으면 정보 저장
                    temp_array[ni][nj] = array[i][j]
                else:                             # 비어있지 않으면 정보를 append하고 마지막에 가장 큰 값 기준 방향으로 저장하자
                    temp_array[ni][nj][0].append(array[i][j][0][0])         # 개수 append
                    temp_array[ni][nj][1].append(array[i][j][1][0])         # 이동 방향 append
                    if [ni,nj] not in temp:                                 # 중복 좌표를 저장
                        temp.append([ni,nj])

    for i,j in temp:                                                        # 중복 좌표들 순회
        max_val=[0,0]
        for max_idx in range(len(temp_array[i][j][0])):
            if max_val[0] < temp_array[i][j][0][max_idx]:
                max_val=[temp_array[i][j][0][max_idx],temp_array[i][j][1][max_idx]]
        temp_array[i][j] = [[sum(temp_array[i][j][0])],[max_val[1]]]        # 가장 큰 개수의 방향으로 방향 설정

    for i in range(N):                              # 모서리 부분의 미생물 수 감소와 방향 변경
        if temp_array[i][0] != 0:
            temp_array[i][0][1][0]= change_dir[temp_array[i][0][1][0]]
            temp_array[i][0][0][0] = temp_array[i][0][0][0] // 2
        if temp_array[i][N-1] != 0:
            temp_array[i][N-1][1][0]= change_dir[temp_array[i][N-1][1][0]]
            temp_array[i][N - 1][0][0] = temp_array[i][N-1][0][0]//2
        if i!=0 and i!=N-1:                     # 겹치는 부분이 중복으로 계산 되지 않게 함
            if temp_array[0][i] != 0:
                temp_array[0][i][1][0]= change_dir[temp_array[0][i][1][0]]
                temp_array[0][i][0][0]=temp_array[0][i][0][0]//2
            if temp_array[N-1][i] != 0:
                temp_array[N-1][i][1][0]= change_dir[temp_array[N-1][i][1][0]]
                temp_array[N - 1][i][0][0]=temp_array[N-1][i][0][0]//2

    return temp_array

delta=((-1,0),(1,0),(0,-1),(0,1))
change_dir=(1,0,3,2)                                # 반대 방향으로 돌리는 용도
T = int(input())
for tc in range(T):
    N,M,K=map(int,input().split())
    arr =[[0]*N for _ in range(N)]
    for _ in range(K):
        i, j, n, move = map(int,input().split())     # i,j,미생물 수, 이동 방향
        arr[i][j]=[[n],[move-1]]                     # 미생물의 위치에 개수와 이동 방향을 저장

    for _ in range(M):                  # M시간 동안 반복
        arr = move_func(arr)            # 함수 내에서 리턴 한 이동 이후 리스트를 arr에 덮어 씌운다

    res = 0                             # 남은 미세물 카운트
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                res+= arr[i][j][0][0]
    print(f'#{tc+1} {res}')