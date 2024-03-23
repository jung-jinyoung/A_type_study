'''
python으로 하면 시간 초과나고 pypy로 하면 통과
시간 612 ms / 메모리 117684 KB
'''

import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
# 각 칸마다 내구성
A = deque(list(map(int, input().split())))
# 로봇이 올라가는 0번부터 내려가는 N번까지만 있으면 됨
robot = deque([0] * N)
stage = 1
while True:
    # (1) 벨트가 각 칸 위에 있는 로봇과 한 칸 회전
    A.rotate(1)
    robot.rotate(1)
    robot[N-1] = 0
    
    # (2) 가장 앞 로봇부터 회전하는 방향으로 한 칸씩 이동
    if robot:
        for i in range(N-2, -1,-1):
            if robot[i] == 1 and robot[i+1] == 0 and A[i+1] >= 1:
                robot[i+1] = 1
                robot[i] = 0
                A[i+1] -= 1
        robot[N-1] = 0
        
    # (3) 조건에 맞춰서 1번 칸에 로봇을 올려
    if robot[0] == 0 and A[0] >= 1:
        robot[0] = 1
        A[0] -= 1
        
    # (4) 
    cnt = 0
    for each in A:
        if each == 0:
            cnt += 1
    if cnt >= K:
        break
    stage += 1

print(stage)
