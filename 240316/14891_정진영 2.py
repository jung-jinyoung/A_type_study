from collections import deque

# 톱니바퀴 회전 함수
def rotate_gear(gear, direction):
    if direction == 1:  # 시계 방향 회전
        gear.appendleft(gear.pop())
    else:  # 반시계 방향 회전
        gear.append(gear.popleft())

# 초기 톱니바퀴 상태 입력
gears = [deque(input()) for _ in range(4)]

# 회전 명령 수 입력
k = int(input())

# 각 회전 명령에 대해 실행
for _ in range(k):
    num, direction = map(int, input().split())
    num -= 1  # 1부터 시작하는 톱니바퀴 번호를 0부터 시작하도록 변환
    directions = [0] * 4  # 각 톱니바퀴마다의 회전 방향을 저장할 리스트 초기화
    directions[num] = direction

    # 왼쪽 톱니바퀴들의 회전 방향 설정
    for i in range(num, 0, -1):
        if gears[i][6] != gears[i - 1][2]:
            directions[i - 1] = -directions[i]
        else:
            break

    # 오른쪽 톱니바퀴들의 회전 방향 설정
    for i in range(num, 3):
        if gears[i][2] != gears[i + 1][6]:
            directions[i + 1] = -directions[i]

    # 각 톱니바퀴를 회전시킴
    for i in range(4):
        if directions[i] != 0:
            rotate_gear(gears[i], directions[i])

# 결과 계산
result = 0
for i in range(4):
    if gears[i][0] == '1':
        result += 2 ** i

print(result)
