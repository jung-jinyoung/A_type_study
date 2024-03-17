"""

순서 :
컨베이어 벨트 회전
-> 로봇 이동
-> 로봇 얹기
-> 내구도 확인


 python 3 : 3520ms/ 34052 KB
 pypy3 : 1132ms/ 117832 KB
"""
from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int,input().split())
conveyor = deque(map(int,input().split()))

robot = deque([0]*N) # 로봇 위치 저장
turn = 0

while True:
    turn += 1

    # 벨트 회전
    conveyor.rotate(1)
    # 벨트 회전에 따른 로봇 위치 이동
    robot.rotate(1)
    robot[-1] = 0 # 로봇 내리기

    # 로봇 존재할 경우 이동
    if sum(robot):
        for i in range(N-2, -1, -1):     # 뒤에서 부터 확인
            if robot[i] == 1 and  robot[i+1] == 0 and conveyor[i+1] >=1:
                robot[i+1] = 1
                robot[i] = 0

                conveyor[i+1] -=1
        # 로봇 내리기
        robot[-1] = 0

    # 로봇 올리기
    # 올리는 위치에 로봇이 없거나 내구도가 0 이 아닌 경우
    if conveyor[0]>=1 and robot[0]==0 :
        # 로봇 올리기
        conveyor[0] -=1
        robot[0] = 1

    # 전체 컨베이어벨트 내구도 확인
    if conveyor.count(0) >=K:
        break

print(turn)

