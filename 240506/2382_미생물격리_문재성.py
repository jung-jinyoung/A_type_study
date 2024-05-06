di = [-1, 1, 0, 0]  # 상, 하, 좌, 우로 이동하기 위한 행 이동값
dj = [0, 0, -1, 1]  # 상, 하, 좌, 우로 이동하기 위한 열 이동값
 
T = int(input())  # 테스트 케이스의 수 입력
for tc in range(1, T+1):
    N, M, K = map(int, input().split())  # 격리 구역의 크기, 시간, 미생물 군집의 수 입력
    microo = {}  # 미생물 군집을 저장할 딕셔너리 생성
    for _ in range(K):
        i, j, num, dir = map(int, input().split())  # 군집의 위치, 수, 이동 방향 입력
        microo[(i, j)] = [num, dir-1]   # 군집의 초기 상태 저장 (상: 0, 하: 1, 좌: 2, 우: 3)
 
    for t in range(M):
        if t == 0:
            copied_microo = microo  # 초기 군집 상태 복사
        else:
            copied_microo = moved_microo  # 이전 시간대의 이동한 군집 상태로 복사
        moved_microo = {}  # 이동한 군집을 저장할 딕셔너리 생성
        for i, j in copied_microo.keys():  # 모든 군집에 대해 반복
            ni, nj = i+di[copied_microo[(i, j)][1]], j+dj[copied_microo[(i, j)][1]]  # 이동 후 위치 계산
            if not (0 < ni < N-1 and 0 < nj < N-1):  # 이동한 위치가 격리 구역 내부가 아닌 경우
                if copied_microo[(i, j)][0] > 1:  # 미생물 수가 1 이상인 경우에만 실행
                    micro_num = copied_microo[(i, j)][0] // 2  # 미생물 수의 반을 구함
 
                    # 이동 방향의 반대 방향을 구함
                    if copied_microo[(i, j)][1] < 2:
                        reversed_dir = (copied_microo[(i, j)][1]+1) % 2
                    else:
                        reversed_dir = (copied_microo[(i, j)][1] + 1) % 2 + 2
 
                    # 이동한 위치에 새로운 군집 정보 추가
                    if (ni, nj) not in moved_microo.keys():
                        moved_microo[(ni, nj)] = [micro_num, reversed_dir]
                    else:
                        moved_microo[(ni, nj)] += [micro_num, reversed_dir]
            else:  # 이동한 위치가 격리 구역 내부인 경우
                # 이동한 위치에 새로운 군집 정보 추가
                if (ni, nj) not in moved_microo.keys():
                    moved_microo[(ni, nj)] = [copied_microo[(i, j)][0], copied_microo[(i, j)][1]]
                else:
                    moved_microo[(ni, nj)] += [copied_microo[(i, j)][0], copied_microo[(i, j)][1]]
 
        for key in moved_microo.keys():  # 군집 정보를 정리하고 최대 미생물 수를 가진 군집을 찾음
            if len(moved_microo[key]) > 2:
                max_micro = 0  # 최대 미생물 수 초기화
                sum_micro = 0  # 미생물 수의 합 초기화
                for m in range(0, len(moved_microo[key]), 2):  # 모든 군집에 대해 반복
                    sum_micro += moved_microo[key][m]  # 미생물 수를 합산
                    if max_micro < moved_microo[key][m]:  # 최대 미생물 수 갱신
                        max_micro = moved_microo[key][m]
                        dir = moved_microo[key][m+1]  # 군집의 이동 방향 저장
                moved_microo[key] = [sum_micro, dir]  # 군집 정보 갱신
 
    result = 0  # 최종 결과 초기화
    for (ni, nj) in moved_microo.keys():  # 모든 군집에 대해 반복하며 미생물 수 합산
        result += moved_microo[(ni, nj)][0]  # 미생물 수를 합산하여 결과에 더함
    print(f'#{tc}', result)  # 결과 출력
