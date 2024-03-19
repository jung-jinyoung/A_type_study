"""
1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다.
    만약 이동할 수 없다면 가만히 있는다.

    1. 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1이상 남아있어야 한다.

3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아감!

종료되었을 때 몇 번째 단계가 진행 중이었는지 구하라. 처음 수행되는 단계는 1단계
"""

from collections import deque

N, K = map(int, input().split())
arr = deque(map(int, input().split()))
robot = deque([0] * N)  # 벨트 위에 있는 로봇
cnt = 0              # 몇 번째 단계인지

while True:
    cnt += 1
    # 1. 컨베이너 벨트 돌리고 하차 지점에 로봇 있으면 내리기
    arr.rotate(1)   # 벨트 1칸씩 회전
    robot.rotate(1) # 로봇도 벨트랑 같이 이동됨
    robot[-1] = 0  # 하차지점 도착시 로봇 하차 -> 하차지점에 로봇이 없더라도 어차피 초기화 해야함

    # 2. 로봇 이동하기. 로봇 다음 칸에 로봇이 없고, 그 칸의 내구도가 1이상 남아있어야함. 먼저 올라간 로봇부터 진행
    for i in range(N-2, -1, -1):
        if robot[i] == 1 and robot[i+1] == 0 and arr[i+1] > 0:
            robot[i], robot[i+1] = robot[i+1], robot[i]     # 로봇 위치 바꾸기
            arr[i+1] -= 1       # 내구도 감소
    robot[-1] = 0   # 하차 지점 로봇 내리기

    # 3. 올리는 자리 내구도 > 0 이면 로봇 올림
    if arr[0] != 0:
        robot[0] = 1    # 로봇 올리기
        arr[0] -= 1

    # 마지막. 0 개수가 K개 이상이면 break

    # 이렇게 했을 떈 python으론 시간초과. pypy론 117684 KB / 624 ms
    # cnt_0 = 0
    # for j in arr:
    #     if j == 0:
    #         cnt_0 += 1
    # if cnt_0 >= K:

    # 이렇게 했을 땐 python으로 34068 KB 3196ms. pypy론 메모리 비슷, 1064 ms
    if arr.count(0) >= K:
        break

print(cnt)