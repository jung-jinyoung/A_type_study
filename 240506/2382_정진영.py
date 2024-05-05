"""
접근 방법 : 시뮬레이션, 구현

1시간씩 지날 때 마다 순서대로 구현
1. 가장자리에는 약품이 칠해져 있다. :(처음에는 미생물 배치 X)
2. 1시간 마다 군집의 이동 //  방향: 상 하 좌 우 => 1 2 3 4
3. 약품이 칠해진 가장 자리에 도착하면 미생물의 절반이 죽는다 : a = a//2
4. 두 개 이상 모이면 합친다 : 방향은 미생물의 수가 더 큰 값의 방향을 따른다.

1. for문 사용 -> 제한시간 초과 :  35개
2. 배열 업데이트 -> 제한시간 초과 : 43개
3. 1+2 합친 후 성공 : 메모리 : 56184 KB, 10643ms ...
"""
import sys
sys.stdin = open('input.in','r')

direction=[(0,0),(-1,0),(1,0),(0,-1),(0,1)]
op = [0,2,1,4,3] # 반대 방향 리스트


T = int(input())
for tc in range(1,T+1):
    N, M, K = map(int,input().split())
    # 셀의 영역 N*N, 격리 시간 M, 미생물 군집 개수 K
    s_info = [] # 미생물 수 저장 리스트
    d_info = [] # 현재 방향 저장 리스트
    p_info = [] # 현재 미생물의 좌표 저장 리스트

    for _ in range(K):
        x, y, n, d = map(int,input().split())
        s_info.append(n) # 초기 미생물의 수 저장
        d_info.append(d) # 초기 방향 저장
        p_info.append((x,y)) # 초기 좌표 저장

    for _ in range(M):
        # 가지치기 : 모든 미생물들이 하나로 합쳐졌다면
        if len(s_info) == 1 :
            break
        p_info = [p_info[i] for i in range(len(s_info)) if s_info[i] !=0]
        d_info = [d_info[i] for i in range(len(s_info)) if s_info[i] !=0]
        s_info = [num for num in s_info if num !=0]

        # 업데이트
        K = len(p_info)
        # 미생물 이동
        for i in range(K):
            # 좌표 확인
            x, y = p_info[i]
            # 방향 확인
            d = d_info[i]

            dx = x + direction[d][0]
            dy = y + direction[d][1]

            # 약품이 칠해진 가장자리에 닿을 경우
            if dx == 0 or dx == N-1 or dy == 0 or dy == N-1:
                d_info[i] = op[d] # 방향 전환
                s_info[i] //= 2 # 미생물 수 절반 처리

            # 좌표 업데이트
            p_info[i] = (dx,dy)

        # 미생물 좌표 확인
        for i in range(K):
            # 가지치기 : 이미 합쳐진 미생물이면 continue
            if s_info[i]==0:
                continue
            x,y = p_info[i]
            if p_info.count((x,y)) >=2 : # 같은 좌표가 2개 이상 발견 된다면
                # 인덱스 찾기
                find_index = [i for i in range(K) if p_info[i] == (x,y)]
                total  = sum(s_info[index] for index in find_index)

                max_index = max(find_index,key = lambda index : s_info[index])

                for idx in find_index:
                    if idx != max_index:
                        s_info[idx] = 0
                s_info[max_index] = total



    print(f'#{tc} {sum(s_info)}')










