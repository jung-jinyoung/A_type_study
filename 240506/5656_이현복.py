import sys
sys.stdin = open('sample_input.txt','r')

# swea_5656_벽돌 깨기
# 메모리 : 73,076 kb
# 실행시간 : 1,554 ms

from collections import deque
import copy
def brick_break(array,idx):                             # idx라는 인덱스에 구슬 던지고 나서의 결과를 리턴
    todo=deque()
    for j in range(H-1,-1,-1):                          # 0 아닌 첫 번째 수의 위치를 체크
        if array[idx][j]>1:
            todo.append((idx,j,array[idx][j]))          # bfs니까 리스트에 넣자
            array[idx][j]=0
            break
        elif array[idx][j] == 1:                        # 1일때는 폭발 없이 이 벽돌만 사라진다 -> 리턴
            array[idx][j] = 0
            return array
    else:                                               # for-else로 이번 라인에 벽돌이 없을 때 -> 리턴
        return array

    while todo:                                         # BFS
        xxx,yyy,break_len=todo.popleft()                # 폭발하는 벽돌의 좌표와 폭발 거리
        for dx,dy in ((1,0),(-1,0),(0,-1),(0,1)):
            for lll in range(1,break_len):
                nx,ny= xxx+dx*lll, yyy+dy*lll
                if 0<=nx<W and 0<=ny<H and array[nx][ny]>0:
                    if array[nx][ny] != 1:              # 터지는 파편이 1이 아니면 append
                        todo.append((nx,ny,array[nx][ny]))
                    array[nx][ny] = 0

    for i in range(W):                                  # 깨진 벽돌 자리를 밀어서 채운다
        for j in range(H - 1, -1, -1):
            if array[i][j]==0:
                array[i].pop(j)
                array[i].append(0)

    return array

def dfs(arrIndfs,level):
    global cnt
    tmp_cnt = 0
    for i in range(W):                                  # 넘어온 리스트에서 0 갯수 카운트
        tmp_cnt += arrIndfs[i].count(0)

    if tmp_cnt==W*H:                                    # 이미 전부 깨진 상태 이면 (전부 0일때) -> 일종의 가지 치기
        cnt = W*H                                       # cnt 를 최대로 갱신 하고 리턴
        return

    if level == N:                                      # 종료 조건
        cnt=max(cnt,tmp_cnt)                            # 이번 깊이 탐색의 0 갯수와 기존 최대값 중 큰 수로 갱신
        return

    for target in range(W):                             # 순회 하면서 하나씩 구슬 던져 보자
        temp = copy.deepcopy(arrIndfs)      # <-- !!!   얉은 복사로 하면 말도 안되는 값이 나와서 깊은 복사 선택함
        dfs(brick_break(temp,target),level+1)

T = int(input())
for tc in range(T):
    N,W,H=map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(H)]
    arr = [[0] * H for _ in range(W)]
    for i in range(H):
        for j in range(W):
            arr[j][H-1-i]=data[i][j]      # 시계방향으로 90도 돌려서 arr에 저장 (같은 행 이어야 순회가 편할 듯 해서)
    cnt = 0
    dfs(arr,0)
    print(f'#{1+tc} {W*H-cnt}')           # cnt가 0의 갯수였다 -> 최대값에서 빼준다