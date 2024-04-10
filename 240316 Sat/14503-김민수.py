"""
-pypy-
메모리 : 109240 KB
시간 : 112ms

-python-
메모리 : 31120 KB
시간 : 44ms
"""
di = [-1, 0, 1, 0]  # 북, 동, 남, 서
dj = [0, 1, 0, -1]  # 북, 동, 남, 서

def pipi(r, c, d):  # 시작 좌표 r,c / 방향
    global cnt

    while True:
        if arr[r][c] == 0:  # 먼지가 있다면
            arr[r][c] = 2  # 청소
            cnt += 1  # 청소 후 cnt+1

        cleaned = False  # 청소를 했는지 여부를 나타내는 변수
        for _ in range(4):  # 네 방향 모두 탐색
            nd = (d + 3) % 4  # 현재 방향에서 왼쪽으로 회전
            ni, nj = r + di[nd], c + dj[nd]
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:  # 청소할 곳이 있다면
                r, c, d = ni, nj, nd  # 이동하고 방향 변경
                cleaned = True  # 청소를 했음을 표시
                break
            else:
                d = nd  # 청소할 곳이 없으면 방향만 변경

        if not cleaned:  # 네 방향 모두 청소할 곳이 없었을 때
            back_d = (d + 2) % 4  # 후진할 방향
            ni, nj = r + di[back_d], c + dj[back_d]
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 1:  # 후진 가능한 경우
                r, c = ni, nj  # 후진
            else:  # 후진할 수 없는 경우 작동 중지
                return

N, M = map(int, input().split())        # 행, 열
r, c, dir = map(int, input().split())   # 처음에 있는 칸의 좌표, 방향
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0        # 청소한 구역 개수
pipi(r, c, dir)
print(cnt)



# di = [-1, 0, 1, 0]  # 북, 동, 남, 서
# dj = [0, 1, 0, -1]  # 북, 동, 남, 서
#
# def pipi(r, c, d):  # 시작 좌표 r,c / 방향
#     global cnt
#
#     while True:
#         if arr[r][c] == 0:  # 먼지가 있다면
#             arr[r][c] = 2  # 청소
#             cnt += 1  # 청소 후 cnt+1
#
#         ni, nj = r+di[d], c+dj[d]
#         if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0:    # 주변에 청소하지 않은 구역이 있을 때
#             d = (d+3)%4    # 반시계 방향으로 90도 회전
#             r, c = ni, nj
#             break
#
#         # 주변에 청소할 구역이 없을 때
#         # 일땐 바라보는 방향을 유지한 채 후진 -> 1번으로 돌아감
#         elif 0<=ni<N and 0<=nj<M and arr[ni][nj] == 2:
#             back_d = (d+2)%4    #후진 할 방향
#             r, c = r+di[back_d], c+dj[back_d]
#             if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 1:  # 후방에 벽이 있다면
#                 return
#             # 후방에 청소한 구역일 때 -> 이미 4방향 탐색을 했으므로 청소안한 구역은 고려할 필요 없음
#             elif 0<=ni<N and 0<=nj<M and arr[ni][nj] == 2:
#                 r, c = ni, nj
#                 continue
#
#
# N, M = map(int, input().split())        # 행, 열
# r, c, dir = map(int, input().split())   # 처음에 있는 칸의 좌표, 방향
# arr = [list(map(int, input().split())) for _ in range(N)]
# cnt = 0        # 청소한 구역
# pipi(r, c, dir)
# print(cnt)
