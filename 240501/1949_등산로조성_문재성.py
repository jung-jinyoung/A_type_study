'''
등산로는 가장 높은 봉우리에서 시작
반드시 높은 지형에서 낮은 지형으로 연결 (대각선 제외)
긴 등산로를 만들기 위해 딱 한 곳을 정해 최대 K 깊이만큼 지형을 깎을 수 있다

N*N 지도, 최대 공사 가능 깊이 K
3 ≤ N ≤ 8
1 ≤ K ≤ 5
지형의 높이는 1 이상 20 이하의 정수
만들 수 있는 가장 긴 등산로를 찾아 길이를 출력

'''
import sys
sys.stdin = open('input.txt', 'r')


# 등산로를 찾는 함수
def hiking(peak, array, visited, level, is_digged):
    global result

    # 현재 등산로의 길이가 최대 등산로의 길이보다 길다면 업데이트
    if result < level:
        result = level
    
    # 현재 위치 빼내서
    row, col = peak
    # 상하좌우로 이동
    for d in range(4):
        nr, nc = row + delta[d][0], col + delta[d][1]
        # 이동한 위치가 지도 범위 내에 있는지 확인
        if 0 <= nr < N and 0 <= nc < N:
            # 이동한 위치를 방문하지 않았고
            if not visited[nr][nc]:
                # 이동한 위치가 현재 위치보다 낮은 높이라면
                if array[nr][nc] < array[row][col]:
                    visited[nr][nc] = 1     # 방문처리
                    # 다음 위치로 이동하며 등산로 길이를 1 증가시키고, 함수를 재귀 호출
                    hiking((nr, nc), array, visited, level + 1, is_digged)
                    visited[nr][nc] = 0     # 방문처리 초기화
                # 이동한 위치가 현재 위치와 같거나 높은 높이일 때, 공사 지금까지 안했으면
                elif not is_digged and array[nr][nc] >= array[row][col]:
                    origin = array[nr][nc]  # 우선 원래 값 저장하고
                    # 최대 공사 가능 깊이까지 반복하여 공사를 시도
                    for k in range(1, K + 1):
                        # 현재 위치의 높이보다 깎인 높이가 작아진 경우
                        if origin - k < array[row][col]:
                            # 현재 위치의 높이를 깎고, 방문 여부를 표시하여 다음 위치로 이동
                            array[nr][nc] = origin - k
                            visited[nr][nc] = 1
                            # 다음 위치로 이동하며 등산로 길이를 1 증가시키고, 함수를 재귀 호출
                            hiking((nr, nc), array, visited, level + 1, True)
                            # 등산로 찾기가 끝나면 현재 위치의 높이와 방문 여부를 원래대로 복구
                            array[nr][nc] = origin
                            visited[nr][nc] = 0
                            break
                    else:   # 공사 안되면 그냥 continue
                        continue


# 상하좌우 이동을 위한 델타 값
delta = ((0, 1), (0, -1), (1, 0), (-1, 0))

# 테스트 케이스 수 입력
T = int(input())
# 각 테스트 케이스에 대한 반복
for tc in range(1, T + 1):
    # 지도 크기 N과 최대 공사 가능 깊이 K 입력
    N, K = map(int, input().split())
    max_v = 0   # 가장 높은 봉우리 찾기
    peak = {}   # 가장 높은 봉우리가 담길 dict (key: 봉우리 높이 - value: 봉우리 좌표 배열)
    arr = []    # 지도가 담길 배열
    # 지도 정보 입력
    for a in range(N):
        tmp = list(map(int, input().split()))
        for b in range(N):
            if max_v < tmp[b]:  # 가장 높은 봉우리의 값 갱신하고 peak를 초기화 후 넣기
                max_v = tmp[b]
                peak.clear()
                peak[max_v] = [(a, b)]
            elif max_v == tmp[b]:   # 같다면 그냥 append
                peak[max_v].append((a, b))
        arr.append(tmp)

    result = 0
    visited = [[0] * N for _ in range(N)]
    # 모든 최고 봉우리에 대해 등산로 탐색
    for each in peak[max_v]:
        visited[each[0]][each[1]] = 1   # 가장 높은 봉우리는 이미 방문처리
        hiking(each, arr, visited, 1, False)
        visited[each[0]][each[1]] = 0   # 초기화
    # 결과 출력
    print(f'#{tc}', result)
