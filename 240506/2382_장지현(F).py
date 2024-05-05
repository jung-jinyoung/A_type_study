'''
tc 46/50
why ㅜㅜㅜ
'''

di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]

chg_dir = [0, 2, 1, 4, 3]


T = int(input())
for tc in range(1, T+1):
    n, m, k = map(int, input().split())
    infos = [list(map(int, input().split())) for _ in range(k)]
    # i, j, micro, dir

    for time in range(m):

        # visited = [[0] * n for _ in range(n)]
        common = []  # 이동한 좌표 저장해서 해당 좌표마다 max 값 & idx 처리

        ## 이동
        for i in range(k):
            if infos[i][2] == 0:   # 사라졌으면 탐색 x
                continue
            
            else:
                dir = infos[i][3]
                
                infos[i][0] += di[dir]  # 이동 좌표 - infos에 바로 갱신
                infos[i][1] += dj[dir]
                
                # 이동한 좌표 입력
                ni = infos[i][0]
                nj = infos[i][1]
                # visited[ni][nj] += 1
                if (ni, nj) not in common:
                    common.append((ni, nj))

                # 약품 구역에 있으면
                if ni == 0 or nj == 0 or ni == n-1 or nj == n-1:
                    infos[i][2] //= 2   # 미생물 빠잉
                    infos[i][3] = chg_dir[infos[i][3]]  # 방향 바꾸기

        # with new infos
        # 현재 시간까지 이동된 좌표들 돌면서, 겹치는 구간 중 가장 큰 값 방향 저장
        for here in common:
            max_micro = 0
            sum_micro = 0
            max_micro_idx = 0 

            for i in range(k):
                if (infos[i][0], infos[i][1]) == here:

                    # 해당 미생물 수 더해주기
                    sum_micro += infos[i][2]

                    # max 정보
                    if max_micro < infos[i][2]:
                        max_micro = infos[i][2]
                        max_micro_idx = i
                    
                    infos[i][2] = 0   # 일단 모인 애들은 (임시로) 없애기
            
            # 그동안 구해진 sum_micro 할당 -- 방향값은 max에게 있음
            infos[max_micro_idx][2] = sum_micro

        ## ififif 약품 & 겹침 동시에 ? -> 그런 경우 (0, 0) (n, 0) 등 .. 은 안나옴

    # 이동, 계산 완료
    answer = 0 
    for info in infos:
        answer += info[2]
    print(f"#{tc} {answer}")