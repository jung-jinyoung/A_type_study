'''
1949. 등산로 조성

등산로를 만들 부지 N*N, 이 곳에 최대 길이의 등산로를 조성하려고 한다.
2차원 배열에서 숫자는 각 지형의 높이

등산로는 가장 높은 봉우리에서 시작
높은 곳에서 낮은 곳으로 이동, 가로와 세로로만 이동
긴 등산로를 만들기 위해 딱 한 곳을 K만큼 깎을 수 있다.

이때 만들 수 있는 가장 긴 등산로를 찾아 그 길이를 출력하라
'''


# 등산로를 건설하는 함수 road
# 매개변수는 각각, 현재의 위치를 나타내는 y와 x, 현재 위치의 높이를 나타내는 height, 분지의 가로와 세로를 나타내는 width, 최대로 깎을 수 있는 높이를 나타낸 can_cut, 지형을 깎았는지 여부를 나타낸 is_cut
def road(y, x, height, length, width, can_cut, is_cut):
    # 글로벌 변수 max_length를 호출
    global max_length
    # 델타를 이용해주려고 합니다.
    for di, dj in [1, 0], [0, 1], [-1, 0], [0, -1]:
        ni = y+di
        nj = x+dj
        # 이동하려는 영역이 분지 안에 위치해 있고, 아직 방문하지 않은 곳이라면
        if 0<=ni<width and 0<=nj<width and visited[ni][nj] == 0:
            # 만약에 이동할 위치가 현재 위치보다 낮다면
            if land[ni][nj] < height:
                # 방문 표시를 해주고
                visited[ni][nj] = 1
                # 다음 함수로 넘어감 여기서 수정해줄 부분은, 이동할 위치의 좌표와 높이, 그리고 등산로의 길이이다.
                road(ni, nj, land[ni][nj], length+1, width, can_cut, is_cut)
                # 재귀가 종료되면 방문했던 곳을 다시 방문하지 않은 것으로 표시
                visited[ni][nj] = 0
            # 만약 현재 위치보다 이동할 위치가 높거나 같다면 일단 한 번 잘라보자,
            # 단, 이동할 위치를 최대로 잘랐을 때 현재 위치보다는 낮아져야 자를 수 있다.
            elif is_cut == 0 and land[ni][nj]-can_cut <= height-1:
                # 방문 표시를 해주고
                visited[ni][nj] = 1
                # 재귀로 넘어갈 때, 수정해줘야할 부분은 다음 좌표와 다음 높이, 등산로의 길이, 그리고 잘랐는지 여부를 이미 잘랐다고 표시
                # 이때, 최대한 등산로를 길게 하려면 최대한 적게 자르는 것이 다음으로 이동하여 등산로를 건설할 수 있느냐 여부를 판단하는데 유리
                # 따라서 높이는 현재 위치에서 1만큼만 잘라줌
                road(ni, nj, height-1, length+1, width, can_cut, 1)
                # 재귀가 종료되면 다시 방문하지 않은 것으로
                visited[ni][nj] = 0
            # 위의 조건을 모두 만족하지 못하면 그 상태가 현재 탐색에서 최대 등산로 길이이므로, 기존의 길이와 비교하여 더 길이가 길면 max_length를 갱신
            else:
                if max_length < length:
                    max_length = length


T = int(input())
# 각 테스트 케이스별 시행
for tc in range(1, T+1):
    # 분지의 가로세로 길이 N과 최대로 깎을 수 있는 높이 K
    N, K = map(int, input().split())
    # 분지의 높이를 2차원 배열로 표시한 land
    land = [list(map(int, input().split())) for _ in range(N)]
    # 높이가 가장 높은 곳들의 좌표를 저장해줄 리스트 top_position
    top_position = []
    # 최대 높이 max_height
    max_height = max(list(map(max, land)))
    # 배열을 순회하며 최대 높이인 값을 저장해준다.
    for i in range(N):
        for j in range(N):
            if land[i][j] == max_height:
                top_position.append((i, j))
    # 등산로의 최대 길이를 저장할 변수 max_length, 초기값은 0
    max_length = 0
    # 등산로를 건설할 때 같은 곳을 방문하지 않도록 표시해줄 2차원 배열 visited
    visited = [[0]*N for _ in range(N)]
    # top_position을 순회하며 함수를 호출
    for position in top_position:
        # 출발점을 방문 표시하고
        visited[position[0]][position[1]] = 1
        road(position[0], position[1], max_height, 1, N, K, 0)
        # 함수 호출이 종료되면 방문 표시를 지워줌
        visited[position[0]][position[1]] = 0
    # 출력 양식에 맞게 출력
    print(f'#{tc} {max_length}')