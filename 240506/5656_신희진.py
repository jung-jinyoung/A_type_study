# 벽돌깨기
'''
1. 구슬은 좌, 우로만 움직일 수 있어서 항상 맨 위에 있는 벽돌만 깨트릴 수 있다
2. 벽돌은 숫자 1 ~ 9 로 표현되며, 구술이 명중한 벽돌은 상하좌우로 ( 벽돌에 적힌 숫자 - 1 ) 칸 만큼 같이 제거된다.
3. 제거되는 범위 내에 있는 벽돌은 동시에 제거된다.
4. 빈 공간이 있을 경우 벽돌은 밑으로 떨어지게 된다.

함수 설명
top_brick_xy > 행을 돌며 가장 윗줄에 있는 벽돌의 x,y값을 구해서 deque로 반환해줌
brick_score > top_brick_xy통해 구슬이 각 위치에 떨어졌을때, 깨지는 벽돌의 개수와 깨지는 벽돌의 좌표값 반환
move_bricks_down > 벽돌을 부신 후 빈공간이 있을 경우 벽돌을 아래로
fin > 위 과정을 반복하는 함수
'''

from collections import deque
from copy import deepcopy

#행을 돌며 가장 윗줄에 있는 벽돌의 x,y값구하기
def top_brick_xy(arr):
    top_brick = deque()
    for i in range(W):
        for j in range(H):
            # 벽돌이 있는 경우 큐에 넣어주고 break
            if arr[j][i] != 0:
                top_brick.append((j, i))
                break
    return top_brick

# x,y값에 구슬이 떨어진 경우 깨트릴 벽돌의 수와, 해당 벽돌의 좌표값 구하기
def brick_score(x,y,arr):
    # 깨지는 벽돌의 수
    # x,y좌표에 구슬은 떨어지므로 기본값 1
    pop_brick = 1
    # 좌우상하 좌표값
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    # bfs를 위한 벽돌 위치 좌표값
    br_list = deque([(x,y)])
    # 한번에 벽돌은 한개이기에 vis로 깨짐 유무를 판단
    vis = [list(0 for __ in range(W)) for _ in range(H)]
    # 떨어지는 위치의 값은 깨짐으로 초기화
    vis[x][y] = 1
    # 깨지는 벽돌 좌표를 담아줄 리스트
    pop_list = []
    while br_list:
        # x,y값 - 현재 위치
        x, y = br_list.popleft()
        # 깨지는 벽돌의 힘
        n_cnt = arr[x][y]
        # 벽돌 좌표에 append
        pop_list.append((x,y))
        # 벽돌의 힘만큼 상하좌우로 힘 전파
        for n in range(1,n_cnt):
            for idx in range(4):
                # 좌표안에 존재하고, 깨지지 않은 벽돌이라면
                if 0<=x+(di[idx]*n)<H and 0<=y+(dj[idx]*n)<W and vis[x+(di[idx]*n)][y+(dj[idx]*n)]==0:
                    # 갈 좌표로 변환 후 방문
                    nx = x+(di[idx]*n)
                    ny = y+(dj[idx]*n)
                    vis[nx][ny] = 1
                    # 갈 곳의 값이 0보다 크다면 == 벽돌이 있다면
                    if arr[nx][ny] > 0:
                        # 깨트릴 벽돌의 수 증가
                        pop_brick += 1
                        # bfs로 넘김
                        br_list.append((nx,ny))
    return pop_brick,pop_list

# 빈 벽돌이 있는 경우 위 벽돌을 아래로 내림
def move_bricks_down(arr):
    for col in range(W):
        # 빈벽돌의 수
        empty_cells = 0
        # 아래서 부터 순회
        for row in range(H - 1, -1, -1):
            # 빈벽돌이라면
            if arr[row][col] == 0:
                empty_cells += 1
            # 빈벽돌이 아니라면 빈벽돌의 수만큼 아래로 내리고
            # 그 위치의 벽돌을 0으로 만듦
            elif empty_cells > 0:
                arr[row + empty_cells][col] = arr[row][col]
                arr[row][col] = 0
    return arr


# 최종 값을 출력하기 위한 함수
def fin(arr, n, cnt, max_cnt, max_arr):
    # N만큼 돈 경우 return을 해주어야 함
    if n > N:
        # 직전에 변경된 arr의 깨진 cnt의 값이 더 크다면
        # cnt와 arr가 정답
        if cnt > max_cnt:
            return cnt, arr
        # 직전에 변경된 arr의 깨진 cnt보다 기존 max_cnt가 크다면
        else:
            return max_cnt, max_arr

    # 구슬이 갈 수 있는 위치를 구한 후 그 곳에 떨어진 경우를 각각 구한 후 재귀
    top_xy = top_brick_xy(arr)
    for xy in top_xy:
        x, y = xy
        # 첫 구슬의 경우 같은 arr를 쓰면 안됨
        # deepcopy이용
        n_arr = deepcopy(arr)
        # 깨트릴 구슬의 개수와, 좌표값
        n_cnt, pop_list = brick_score(x, y, n_arr)
        # 좌표값을 돌면서 0으로 만들어줌
        for px, py in pop_list:
            n_arr[px][py] = 0
        # 빈 공간이 있는 경우 벽돌을 아래로 내려줌
        n_arr = move_bricks_down(n_arr)
        # 재귀를 돌면서 값을 받아준다
        # 변경된 n_arr, 구슬+1, 깨트릴 구슬의 개수를 더해줌, 많이 깨트린 구슬의 수와, 많이 깨트린 arr도 함께 리턴
        result_cnt, result_arr = fin(n_arr, n + 1, cnt + n_cnt, max_cnt, max_arr)
        # max_cnt보다 방금 변경된 값이 더 크다면
        # max_cnt와 max_arr를 변경해줌
        if result_cnt > max_cnt:
            max_cnt = result_cnt
            max_arr = result_arr
    # 더 큰값을 반환
    return max_cnt, max_arr

T = int(input())
for tc in range(T):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    max_cnt, max_arr = fin(arr, 1, 0, 0, None)
    res = 0
    if max_arr:
        for i in range(H):
            for j in range(W):
                if max_arr[i][j] != 0:
                    res += 1
    print(f'#{tc+1}',res)
