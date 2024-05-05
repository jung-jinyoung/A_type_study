
from collections import deque
from copy import deepcopy

def top_brick_xy(arr):
    top_brick = deque()
    for i in range(W):  # 행을 먼저 돌면서 가장 윗줄에 있는 벽돌의 위치를 찾음
        for j in range(H):
            if arr[j][i] != 0:
                top_brick.append((j, i))
                break
    return top_brick


def brick_score(x,y,arr):
    pop_brick = 1
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    br_list = deque([(x,y)])
    vis = [list(0 for __ in range(W)) for _ in range(H)]
    vis[x][y] = 1
    pop_list = []
    while br_list:
        x, y = br_list.popleft()
        n_cnt = arr[x][y]
        pop_list.append((x,y))
        for n in range(1,n_cnt):
            for idx in range(4):
                if 0<=x+(di[idx]*n)<H and 0<=y+(dj[idx]*n)<W and vis[x+(di[idx]*n)][y+(dj[idx]*n)]==0:
                    nx = x+(di[idx]*n)
                    ny = y+(dj[idx]*n)
                    vis[nx][ny] = 1
                    if arr[nx][ny] > 0:
                        pop_brick += 1
                        br_list.append((nx,ny))

    return pop_brick,pop_list

def move_bricks_down(grid):
    for col in range(len(grid[0])):
        empty_cells = 0
        for row in range(len(grid) - 1, -1, -1):
            if grid[row][col] == 0:
                empty_cells += 1
            elif empty_cells > 0:
                grid[row + empty_cells][col] = grid[row][col]
                grid[row][col] = 0
    return grid


T = int(input())
for tc in range(T):
    N, W, H = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(H)]
    for n in range(N):
        cnt = 0
        # n_arr = deepcopy(arr)
        # print(n_arr)
        top_xy = top_brick_xy(arr)
        select = 0
        select_pop_list = 0
        print(n,'번째 벽돌깨기중')
        for xy in top_xy:
            x,y = xy
            max_cnt, pop_list = brick_score(x,y,arr)
            if max_cnt > select:
                select_pop_list = pop_list

        for rm in range(len(select_pop_list)):
            px,py = select_pop_list[rm]
            arr[px][py] = 0

        arr = move_bricks_down(arr)
    print(arr)
    # print(arr)

