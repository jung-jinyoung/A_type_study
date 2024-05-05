"""

1. 20개 맞음
2. Arr 를 빈 리스트로 수정 -> 저장 오류를 피하기 위함
3. 같은 충전기인지 파악하기 위해 인덱스와 함께 arr에 저장
4. 비교 후 저장

복기
1. 인덱스가 같을 때가 같은 충전기 사용인데 충전양으로 비교함
2. sorted하는 과정에서 복잡해져서 헷갈리기 시작 -> 여기서 많이 헤맴
3. 다음부터는 다중 리스트를 0,-1로 채우는 게 아니라 빈 리스트로도 채우는 방법을 생각해볼 수 있겠다.
4. bfs로 마름모를 돌 수도 있다.

제출 :
메모리 : 50936kb
시간 : 216ms
"""

import sys
sys.stdin = open('input.in','r')


directions = [(0,0),(-1,0),(0,1),(1,0),(0,-1)] # 이동방향 정보에 따른 인덱스 설정 (정지, 상, 우, 하, 좌)
T = int(input())

for tc in range(1,T+1):
    # 총 이동시간 M, 충전기의 개수 A
    M, A = map(int, input().split())
    # A, B 두 사람의 이동 정보 ( A  : (1,1) 출발 / B : (10,10) 출발

    info_A = [0] + list(map(int,input().split()))
    info_B =[0] + list(map(int,input().split()))

    arr = [[[]  for _ in range(10)] for _ in range(10)] # 빈 리스트로 수정


    # 충전기 정보 입력
    for i in range(A):
        y, x, c, p = map(int, input().split())
        x, y = x-1,y-1

        # 충전기 좌표 (x,y) 충전 범위 c, 처리량 p
        for nx in range(x-c,x+c+1):
            if not (0<=nx<10):
                continue
            for ny in range(y-c,y+c+1):
                if 0<=nx<10 and 0<=ny<10 :
                    # 거리 확인
                    d = abs(x-nx) + abs(y-ny)
                    if d > c :
                        continue
                    if d <=c :
                        arr[nx][ny].append([p,i])
    # M 시간 동안 이동

    ai, aj = 0, 0
    bi, bj = 9, 9

    total = 0
    for m in range(M+1):
        ai += directions[info_A[m]][0]
        aj += directions[info_A[m]][1]
        bi += directions[info_B[m]][0]
        bj += directions[info_B[m]][1]

        if arr[ai][aj]  and not arr[bi][bj]  :
            total += sorted(arr[ai][aj], reverse=True)[0][0]
        elif arr[bi][bj]  and not arr[ai][aj]:
            total += sorted(arr[bi][bj], reverse=True)[0][0]
        elif arr[ai][aj] and arr[bi][bj]:
            sorted_a = sorted(arr[ai][aj], reverse=True)
            sorted_b = sorted(arr[bi][bj], reverse=True)
            if sorted_a[0][1] == sorted_b[0][1]:
                total += sorted_a[0][0]
                if len(sorted_a) > 1 and len(sorted_b) == 1 :
                    total += sorted_a[1][0]
                elif len(sorted_b)>1 and len(sorted_a) == 1:
                    total += sorted_b[1][0]
                elif len(sorted_a)>1 and len(sorted_b) >1:
                    total += max(sorted_a[1][0], sorted_b[1][0])
            else:
                total += sorted_a[0][0] + sorted_b[0][0]
    print(f'#{tc} {total}')











