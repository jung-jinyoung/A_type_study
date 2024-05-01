'''
홈방범 서비스
마름모 영역에서만 제공됨
운영비용 필요 - 서비스 영역의 크기 K 가 커질수록 증가
운영비용 = K**2 + (K-1)**2

서비스 제공받는 집들은 각각 M의 비용만큼 제공
도시 크기 N     5 ≤ N ≤ 20
하나의 집이 지불할 수 있는 비용 M    1 ≤ M ≤ 10
도시의 정보가 주어질 때,

손해를 보지 않으면서 홈방범 서비스를 가장 많은 집들에 제공하는 서비스 영역을 찾고
그때, 서비스를 제공받는 집들의 수를 출력!



'''
import sys
sys.stdin = open('input.txt', 'r')

# 테스트 케이스 수 입력
T = int(input())
# 각 테스트 케이스에 대한 반복
for tc in range(1, T + 1):
    # 도시 크기 N과 집이 지불할 수 있는 비용 M 입력
    N, M = map(int, input().split())
    # 도시의 개수 세기
    cnt_house = 0
    # 도시의 정보 입력
    arr = []
    for a in range(N):
        tmp = list(map(int, input().split()))
        for b in range(N):
            if tmp[b]:
                cnt_house += 1
        arr.append(tmp)
    # 결과 초기화
    result = 0

    # 서비스 가능한 모든 마름모 영역에 대해 거꾸로 반복한다
    for k in range(N+2, 0, -1):
        # 운영비용 계산
        cost = k**2 + (k-1)**2

        # 전체 집들로 구한 매출보다 운영비용이 크면 continue -> 더 작은 영역을 고려한다
        if cnt_house * M < cost:
            continue

        # 서비스 영역의 좌표들의 개수보다 이미 구해진 result가 더 크면 더 이상 고려하지 않는다
        if cost < result:
            break

        # 서비스 좌표를 저장할 배열
        service = []
        # 현재 마름모 영역에 대한 서비스 좌표 생성
        start_i, start_j, end_j = 0, 0, 0
        for i in range(start_i-k+1, start_i+k):
            for j in range(start_j, end_j+1):
                # 서비스 좌표 저장
                service.append((i, j))
            # 마름모 영역의 시작과 끝 인덱스 업데이트
            if i < start_i:
                start_j -= 1
                end_j += 1
            else:
                start_j += 1
                end_j -= 1

        # 각 집에 대해 서비스 영역 내의 집 개수 세기
        for r in range(N):
            for c in range(N):
                cnt = 0
                for each in service:
                    nr, nc = each[0]+r, each[1] + c
                    # 서비스 영역 내에 있고, 집이 있다면 카운트 증가
                    if 0 <= nr < N and 0 <= nc < N:
                        if arr[nr][nc]:
                            cnt += 1
                # 최대 서비스 가능 집 수를 넘지 않으면서, 현재 집 개수가 최대인 경우 결과 갱신
                if result < cnt and cost <= cnt * M:
                    result = cnt

    # 결과 출력
    print(f'#{tc}', result)

