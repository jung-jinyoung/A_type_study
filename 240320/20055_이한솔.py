# 컨베이어 벨트 위의 로봇
'''
1번칸 : 올리는 위치
N번칸 : 내리는 위치
내리는 위치 도달 : 내림
올리는 위치에 올리거나 이동시 내구도 -1

이동하려는 칸에 로봇이 없고 내구도가 1이상이어야 이동 가능
내구도가 0인 칸의 개수가 K개 이상이라면 과정 종료
'''
from collections import deque
N,K = map(int,input().split())
# 내구도 리스트
du = deque(list(map(int, input().split())))
# 로봇 리스트
robot = deque([0]*N)
res = 0

while 1:
    du.rotate(1)        # rotate(1) => 오른쪽으로 이동 // 제일 뒤에 있던 요소가 제일 앞으로 이동
    robot.rotate(1)     # robot 도 동일하게 이동
    robot[-1] = 0       # 맨 마지막은 내리는 곳이므로 0
    
    if sum(robot):      # 로봇이 하나라도 있으면
        for i in range(N-2,-1,-1):       # 내리는 곳의 인덱스 : N-1 이므로 N-2 부터 맨 처음 요소까지 뒤에서 앞으로 
            if robot[i] == 1 and robot[i+1] == 0 and du[i+1]>=1:       # 로봇이 있고 그 뒤에 칸이 비어있고 뒷 칸의 내구도이 1 이상이면
                robot[i+1] = 1      # 한 칸 이동
                robot[i] = 0        
                du[i+1] -= 1        # 로봇 올린 곳의 내구도 -1

        robot[-1] = 0       # 내리는 곳에서 로봇 내림
    
    if robot[0] == 0 and du[0] >= 1:        # 올리는 곳에 로봇이 없고 올리는 곳의 내구도이 1이상이면
        robot[0] = 1        # 로봇 올림
        du[0] -= 1      # 내구도 -1
    res += 1
    
    if du.count(0) >= K:        # 내구도가 0인 칸이 K개 이상이면 종료
        break

print(res)
