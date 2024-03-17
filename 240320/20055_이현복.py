import sys
sys.stdin = open('sample_input.txt','r')

'''
20055_컨베이어 벨트 위의 로봇
pypy3 : 115452KB/312ms
python3 :34036KB/3392ms

시간초과로 6번정도 제출한듯 ...
바꾼 부분 1 : 로봇 위치도 deque로 받아서 rotate돌리고 0자리에 0 넣던 방법을 일반 리스트에서 pop,insert로 교체
바꾼 부분 2 : 마지막 break조건을 A.count == K 로 했던것을 내구도 감소시 마다 0인지 확인하는 방법으로 교체

### 위 두 부분을 같이 바꾸니 통과
'''
from collections import deque

N,K = map(int,input().split())
A = deque(map(int,input().split()))
# robot=deque([0]*N)
robot=[0]*N

step=0
cnt = 0
while 1:
    step += 1

    # 1단계
    A.rotate(1)
    # robot.retate(1)
    # robot[0]=0
    robot.pop()
    robot.insert(0,0)

    # 2단계
    robot[N-1]=0
    for i in range(N-1,0,-1):
        if robot[i-1]==1 and robot[i]==0 and A[i]>0:
            robot[i-1],robot[i]=0,1
            A[i]-=1
            if A[i]==0: cnt+=1

    # 3단계
    if A[0] != 0:
        robot[0]=1
        A[0]-=1
        if A[0]==0: cnt+=1

    # 4단계
    if cnt >= K:
        break
print(step)
    