import sys
sys.stdin = open('sample_input.txt','r')

'''
240411_no_2_도로 건설하기

'''

T = int(input())
for tc in range(T):
    W,H=map(int,input().split())
    arr = [list(map(int,input().split()))for _ in range(H)]
    house = []
    garo = []                               # - 가로로 생기는 다리 없는 인덱스
    sero = []                               # | 세로로 생기는 다리 없는 인덱스
    degak1 = []                             # / 좌하에서 우상으로 생기는 다리 없는 인덱스
    degak2 = []                             # \ 우하에서 좌상으로 생기는 다리 없는 인덱스

    for i in range(H):
        for j in range(W):
            if arr[i][j]==1:                # 집 기준으로
                house.append((i,j))         # 집 위치 저장
                garo.append(i)              # 다리가 생길 수 없는 인덱스 모음
                sero.append(j)
                degak1.append(j+i)
                degak2.append(j-i)
    garo,sero = set(garo),set(sero)         # 중복 제거를 위해 set로 덮기
    degak1,degak2 = set(degak1),set(degak2)
    bridge1 = [i for i in range(H) if i not in garo]        # 다리가 생길 수 있는 인덱스의 리스트 생성
    bridge2 = [i for i in range(W) if i not in sero]
    bridge3 = [i for i in range(1,(H-1)+(W-1)) if i not in degak1]
    bridge4 = [i for i in range(1-(H-1),W-1) if i not in degak2]

    distance1 = distance2 = 0
    distance3 = [0] * (W + H)
    distance4 = [0] * (W + H)
    for x, y in house:              # 집 하나씩 거리계산 해보자
        if bridge1:
            for i in bridge1:                           # 다리 1,2는 가로, 세로라서 거의 동일
                distance1 = max(distance1, abs(i - x))  # 이번 다리에서 가장 먼 집 거리 저장
        else: distance1 = W * H     # 다리가 없으면 최대값보다 큰거 넣어 놓자

        if bridge2:
            for j in bridge2:
                distance2 = max(distance2, abs(j - y))
        else: distance2 = W * H


        if bridge3:                                     # 다리 3,4는 대각선이라서 거의 동일
            for k in bridge3:                           # 다리 위치 순회
                temp3_d = W + H
                for i in range(H):
                    for j in range(W):
                        if j+i==k:                                      # 합이 k인 대각선이면
                            temp3_d = min(temp3_d,abs(x-i)+abs(y-j))    # 최솟값을 이번 집의 다리까지 최소거리 구한다
                distance3[k]=max(distance3[k],temp3_d)                  # 집을 순회하는 반복문이 가장 상위라서 각 k 다리일때끼리 모아서 max 뽑는다
        else: distance3 = W * H

        if bridge4:
            for k in bridge4:
                temp4_d = W + H
                for i in range(H):
                    for j in range(W):
                        if j-i==k:
                            temp4_d = min(temp4_d,abs(x-i)+abs(y-j))
                distance4[k+H+1]=max(distance4[k+H+1],temp4_d)
        else: distance4 = W * H

    if distance3 != W * H: distance3 = list(set(distance3))[1]  # 3방향으로 다리가 하나 이상 존재 가능 했으면 0이아닌 최소값 뽑는다
    if distance4 != W * H: distance4 = list(set(distance4))[1]  # (리스트 넉넉하게 만들어서 빈자리에 0이 있음)
    res =min(distance1,distance2,distance3,distance4)           # 각 방향의 다리까지 최대 거리 중 최소인거 뽑기
    if res == W * H:                                            # 다리를 만들지 못 하는 경우는 -1 뽑자
        res = -1
    print(f'#{tc+1} {res}')


