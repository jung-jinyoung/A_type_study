'''
무선 충전 최적 배터리 선택 알고리즘
이 알고리즘은 사용자 A와 B가 이동하는 동안 최적의 충전기를 선택하여 충전량을 최대화합니다.

입력:
- T: 테스트 케이스의 수
- M: 총 이동 시간
- N: 충전기의 개수
- route_A: 사용자 A의 이동 경로
- route_B: 사용자 B의 이동 경로
- chargers: 충전기의 위치와 성능 정보를 담은 리스트

출력:
각 테스트 케이스별로 모든 사용자가 충전한 양의 합의 최댓값을 출력합니다.

추가 설명:
- 사용자가 지도 밖으로 이동하는 경우는 없습니다.
- 만약 한 충전기에 두 사용자가 접속한다면, 접속한 사용자의 수만큼 충전 양이 균등하게 분배됩니다.
- 충전 범위 내에 있으면 접속할 수 있으며, 충전 범위가 겹치는 경우에는 가장 성능이 좋은 충전기를 선택합니다.
'''

import sys
sys.stdin = open('input.txt', 'r')

# 상, 우, 하, 좌로 이동하는 경우의 좌표 변화값
delta = ((0, 0), (-1, 0), (0, 1), (1, 0), (0, -1))

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    M, N = map(int, input().split())  # 총 이동 시간, 충전기의 개수
    route_A = list(map(int, input().split()))  # 사용자 A의 이동 경로
    route_B = list(map(int, input().split()))  # 사용자 B의 이동 경로
    chargers = []  # 충전기 정보를 담을 리스트
    for _ in range(N):
        x, y, C, P = map(int, input().split())  # 충전기의 위치와 성능 정보
        chargers.append((y-1, x-1, C, P))  # (y, x) 좌표로 변환하여 리스트에 추가

    # 초기 사용자 A와 B의 위치, 초기 시간, 결과 초기화
    now_A = (0, 0)
    now_B = (9, 9)
    time = 0
    result = 0

    while time <= M:  # 이동 시간이 M보다 작거나 같을 때까지 반복
        connect_A, connect_B = [], []  # 사용자 A와 B가 접속 가능한 충전기를 담을 리스트
        cnt_A, cnt_B = 0, 0  # 사용자 A와 B가 접속한 충전기의 개수 초기화

        # 사용자 A와 B의 위치에 따라 접속 가능한 충전기 찾기
        for charger in chargers:
            if abs(now_A[0] - charger[0]) + abs(now_A[1] - charger[1]) <= charger[2]:
                connect_A.append(charger)
                cnt_A += 1
            if abs(now_B[0] - charger[0]) + abs(now_B[1] - charger[1]) <= charger[2]:
                connect_B.append(charger)
                cnt_B += 1

        # 사용자 A와 B가 각각 한 개의 충전기에만 접속한 경우
        if cnt_A == 1:
            selected_A = connect_A[0]
        elif cnt_A > 1:
            connect_A.sort(key=lambda x: x[3], reverse=True)  # 충전기의 성능을 기준으로 내림차순 정렬
            selected_A = connect_A[0]
        elif cnt_A == 0:
            selected_A = (0, 0, 0, 0)  # 접속할 충전기가 없는 경우 (0, 0, 0, 0)으로 선택

        if cnt_B == 1:
            selected_B = connect_B[0]
        elif cnt_B > 1:
            connect_B.sort(key=lambda x: x[3], reverse=True)  # 충전기의 성능을 기준으로 내림차순 정렬
            selected_B = connect_B[0]
        elif cnt_B == 0:
            selected_B = (0, 0, 0, 0)  # 접속할 충전기가 없는 경우 (0, 0, 0, 0)으로 선택

        # 사용자 A와 B가 같은 충전기에 접속한 경우
        if selected_A == selected_B:
            if cnt_A > 1 and cnt_B > 1:  # 둘 다 다른 후보 충전기가 있는 경우
                if connect_A[1][3] > connect_B[1][3]:  # A의 두 번째 후보 충전기의 성능이 더 좋은 경우
                    selected_A = connect_A[1]
                else:  # B의 두 번째 후보 충전기의 성능이 더 좋은 경우
                    selected_B = connect_B[1]
            elif cnt_A == 1 and cnt_B > 1:  # A만 한 개의 충전기에 접속한 경우
                selected_B = connect_B[1]  # B는 두 번째 후보 충전기 선택
            elif cnt_B == 1 and cnt_A > 1:  # B만 한 개의 충전기에 접속한 경우
                selected_A = connect_A[1]  # A는 두 번째 후보 충전기 선택
            elif cnt_A == 1 and cnt_B == 1:  # A와 B가 모두 한 개의 충전기에 접속한 경우
                selected_A = (-1, -1, 0, 0)  # 서로 충전량을 분배할 필요 없음

        # 결과에 사용자 A와 B가 접속한 충전기의 성능을 더함
        result += selected_A[3] + selected_B[3]
        if time < M:
            now_A = (now_A[0]+delta[route_A[time]][0], now_A[1]+delta[route_A[time]][1])
            now_B = (now_B[0]+delta[route_B[time]][0], now_B[1]+delta[route_B[time]][1])
        time += 1
 
    print(f'#{tc}', result)

       
