# python3 : 56ms, pypy : 132ms
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 방향: 0 : >, 1 : ^, 2 : <, 3 : v
delta_dragon = ((0, 1), (-1, 0), (0, -1), (1, 0))   # 드래곤 커브가 x와 y 좌표를 이동하는 방향
arr = [[0]*101 for _ in range(101)]     # 101x101 그리드를 모두 0으로 초기화
N = int(input())    # 드래곤 커브의 개수를 읽음

for l in range(N):
    x, y, d, g = map(int, input().split())  # 시작 위치 (x, y), 초기 방향 (d), 세대 (g)를 읽음

    level = 0   # 현재 드래곤 커브의 세대를 0 으로 초기화하고 레벨 0의 드래곤 커브를 수행한다
    arr[y][x] = 1   # 그리드에서 시작점을 찍는다
    nr, nc = y + delta_dragon[d][0], x + delta_dragon[d][1]     # 초기 방향을 기반으로 다음 점 계산
    arr[nr][nc] = 1     # 그리드에서 0세대의 다음 점을 찍는다
    nd = (d + 1) % 4    # 첫 번째 이동 후의 새로운 방향 계산 (우회전해서 그려야 함)
    path = [nd]     # 이동한 방향을 저장하는 리스트 초기화
    y, x = nr, nc   # 끝점으로 현재 위치를 업데이트

    while level < g:    # 레벨이 0 이상일 경우, 반복해서 드래곤 커브를 그린다.

        level += 1  # 드래곤 커브의 세대를 하나씩 올리며 진행한다.

        for k in range(len(path) - 1, -1, -1):  # 이전까지 입력된 경로에서 거꾸로 하나씩 진행해야 한다.
            heading = delta_dragon[path[k]]     # 경로에 따라 이동할 방향 가져오기
            ny, nx = y + heading[0], x + heading[1]     # 이동 방향을 기반으로 다음 점 계산
            arr[ny][nx] = 1     # 그리드에서 다음 점을 찍는다
            path.append((path[k]+1) % 4)    # 오른쪽으로 회전하여 다음 세대를 위해 경로를 업데이트 해준다
            y, x = ny, nx   # 현재 위치를 업데이트

delta_square = ((0, 0), (0, 1), (1, 0), (1, 1))     # 정사각형의 네 꼭짓점 상대 좌표
cnt = 0     # 출력할 네 꼭지점이 모두 드래곤 커브의 일부인 정사각형의 개수
for i in range(100):
    for j in range(100):
        for dot in range(4):
            ni, nj = i + delta_square[dot][0], j + delta_square[dot][1]
            if not arr[ni][nj]:     # 꼭지점이 드래곤 커브의 일부가 아니면 바로 다음 정사각형을 고려한다
                break
        else:   # break 없이 for문을 무사히 빠져나온 경우 : 정답에 해당하는 정사각형이므로 cnt 1 증가
            cnt += 1
print(cnt)  # 정답을 출력한다

'''
드래곤 커브
x 축은 > 방향 : 열
y 축은 v 방향 : 행
(y, x)의 개념으로 생각해야 함

0세대 드래곤 커브는 길이가 1인 선분
1세대 드래곤 커브는 시계방향으로 90도 회전 후 끝점에 붙인다
2세대 드래곤 커브도 마찬가지
즉, K세대 드래곤 커브는 K-1세대 드래곤 커브의 끝 점을 기준으로
90도 시계 방향 회전 후 끝점에 붙임

크기가 100×100인 격자 위에 드래곤 커브가 N개 있다.
크기가 1×1인 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 정사각형의 개수를 구하시오

입력
드래곤 커브의 개수 N : 1 ≤ N ≤ 20
둘째 줄에서 N개의 줄에 드래곤 커브의 정보가 주어짐
x, y 시작점, d 시작 방향, g 세대 로 이루어짐 : (0 ≤ x, y ≤ 100, 0 ≤ d ≤ 3, 0 ≤ g ≤ 10)
0 >
1 ^
2 <
3 v

> : ^
^ : <
< : v
^ : <
'''
