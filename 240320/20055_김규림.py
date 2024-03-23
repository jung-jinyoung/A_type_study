from collections import deque

n, k = map(int, input().split())
arr = deque(map(int, input().split()))  # 내구도. A1, A2, ..., A2N
robot = deque([0] * n)                  # 벨트 위에 있는 로봇
result = 0

while True:
    result += 1

    arr.rotate(1)     # 컨베이어 벨트 회전
    robot.rotate(1)
    robot[-1] = 0    # 내리는 위치에 오면 내림

    for i in range(n - 2, -1, -1):      # 로봇 이동 / 먼저 올라간 로봇부터 진행

        # 다음 내구도 1이상인 지, 다음 위치에 로봇 없는지, 현재 위치에 로봇 있는지
        if arr[i + 1] >= 1 and robot[i + 1] == 0 and robot[i] == 1:
            robot[i + 1] = 1
            robot[i] = 0
            arr[i + 1] -= 1
    robot[-1] = 0           # 내리는 위치에 도달한 경우, 내림

    # 올리는 위치에 내구도 0 아니고 로봇 없으면 로봇 올리기 / 내구도 감소
    if arr[0] != 0 and robot[0] != 1:
        robot[0] = 1
        arr[0] -= 1

    # 내구도 0인 칸 수가 k이상이면 종료
    if arr.count(0) >= k:
        break

print(result)