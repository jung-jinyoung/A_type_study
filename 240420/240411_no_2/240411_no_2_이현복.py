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
    garo = []       # - 가로로 생기는 다리 없는 인덱스
    sero = []       # | 세로로 생기는 다리 없는 인덱스
    degak1 = []     # / 좌하에서 우상으로 생기는 다리 없는 인덱스
    degak2 = []     # \ 우하에서 좌상으로 생기는 다리 없는 인덱스

    for i in range(H):
        for j in range(W):
            if arr[i][j]==1:
                house.append((i,j))
                garo.append(i)
                sero.append(j)
                degak1.append(j+i)
                degak2.append(j-i)
    garo,sero = set(garo),set(sero)
    degak1,degak2 = set(degak1),set(degak2)
    bridge1 = [i for i in range(H) if i not in garo]
    bridge2 = [i for i in range(W) if i not in sero]
    bridge3 = [i for i in range(1,(H-1)+(W-1)) if i not in degak1]
    bridge4 = [i for i in range(1-(H-1),W-1) if i not in degak2]

    distance1 = distance2 = 0
    distance3 = [0] * (W + H)
    distance4 = [0] * (W + H)
    for x, y in house:
        if bridge1:
            for i in bridge1:
                distance1 = max(distance1, abs(i - x))
        else: distance1 = W * H

        if bridge2:
            for j in bridge2:
                distance2 = max(distance2, abs(j - y))
        else: distance2 = W * H


        if bridge3:
            for k in bridge3:
                temp3_d = W + H
                for i in range(H):
                    for j in range(W):
                        if j+i==k:
                            temp3_d = min(temp3_d,abs(x-i)+abs(y-j))
                distance3[k]=max(distance3[k],temp3_d)
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

    if distance3 != W * H: distance3 = list(set(distance3))[1]
    if distance4 != W * H: distance4 = list(set(distance4))[1]
    res =min(distance1,distance2,distance3,distance4)
    if res == W * H:
        res = -1
    print(f'#{tc+1} {res}')


