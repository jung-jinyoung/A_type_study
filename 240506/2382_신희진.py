'''
오답
채점용 input 파일로 채점한 결과 fail 입니다.
(오답 : 50개의 테스트케이스 중 49개가 맞았습니다.)
하..........................................
'''
from copy import deepcopy

T = int(input())
for tc in range(T):
    # 세로 위치, 가로 위치, 미생물 수, 이동 방향
    N, M, K = map(int, input().split())
    # 받을 데이터
    arr = [[0] * N for _ in range(N)]
    # 변경을 위한 데이터
    n_arr = [[0] * N for _ in range(N)]
    # 입력 데이터를 arr에 반영하기
    # 미생물이 있는 경우 위치에 [미생물의 개수, 방향]을 넣어줌
    # 방향의 경우 idx로 접근하기 위해 -1을 해줌
    for i in range(K):
        x, y, n, d = map(int, input().split())
        arr[x][y] = [n, d - 1]

    # 상하좌우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    # 방향 전환을 위한 딕셔너리 값
    # 약품에 간 경우 방향을 반대로 해줘야 함 > 이때 사용
    ro = {0: 1, 1: 0, 2: 3, 3: 2}

    # 시간만큼 돌려줌
    for t in range(M):
        # 내가 갈 위치에 모일 미생물을 구하기 위한 딕셔너리
        dic = {}
        # arr를 순회
        for i in range(N):
            for j in range(N):
                # 값이 0이 아닌 경우 == 미생물이 있는 경우
                if arr[i][j] != 0:
                    # 미생물의 수, 방향
                    n, d = arr[i][j][0], arr[i][j][1]
                    # 내가 가고자 하는 위치
                    ni, nj = i + di[d], j + dj[d]
                    # 그 위치의 값이 범위 내에 있는지 보기
                    if 0 <= ni < N and 0 <= nj < N:
                        # 딕셔너리의 키값은 변경불가능한 값이 들어가야 해서 str으로
                        key = str([ni, nj])
                        # 해당 키가 없다면 키를 만들어 주고 값을 넣어줌
                        if key not in dic:
                            dic[key] = [(i, j)]
                        # 키 값이 있다면 값만 넣어줌
                        else:
                            dic[key].append((i, j))


        for key in dic:
            # str을 좌표 값으로 변환
            x, y = map(int, key[1:-1].split(','))
            # 한곳에 여러 미생물이 모일 경우 최대의 미생물을 구하기 위한 max_n
            # 미생물 값을 다 더할 num
            # 최대 미생물의 방향값 nd
            max_n = 0
            num = 0
            nd = 0
            # 미생물이 약품란에 있다면
            if x == 0 or x == N - 1 or y == 0 or y == N - 1:
                rex, rey = dic[key][0]
                num = arr[rex][rey][0]
                nd = arr[rex][rey][1]
                # 값을 반으로 나눠줌, 방향 전환
                n_arr[x][y] = [num // 2, ro[nd]]
            # 그렇지 않다면
            else:
                for li in dic[key]:
                    rex, rey = li
                    # 미생물을 다 더해줌
                    num += arr[rex][rey][0]
                    # 최대 미생물에 대한 방향값 가져오기
                    if arr[rex][rey][0] > max_n:
                        max_n = arr[rex][rey][0]
                        nd = arr[rex][rey][1]
                # 새로운 리스트에 값을 넣어줌
                n_arr[x][y] = [num, nd]
        # arr에 변경된 값으로 할당
        arr = deepcopy(n_arr)
        # n_arr 초기화
        n_arr = [[0] * N for _ in range(N)]

    # 최종 값 구하기
    total = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                total += arr[i][j][0]
    print("#{} {}".format(tc + 1, total))
