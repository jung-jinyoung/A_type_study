"""
풀지 못함 ..

"""


from collections import deque

def turn_on(d,n):
    tmp= [-1]*8

    if d == 1:
        # 시계 방향 회전
        for i in range(8):
            tmp[(i + 1) % 8] = gears[n][i]
    else:
        # 반시계 방향 회전
        for i in range(8):
            tmp[i] = gears[n][(i + 1) % 8]
    gears[n] = tmp




# 톱니 바퀴 상태
# 인덱스 설정을 위한 더미 생성
gears =[[]]+ [list(input()) for _ in range(4)]

K = int(input()) # 회전 횟수
info = deque()
for _ in range(K):
    # 회전 시킨 번호 , 방향  (1 시계, -1 반시계)
    num, di = map(int,input().split())
    info.append((num,di))

directions = [0]*5
while info :
    n ,d = info.popleft()
    directions[n] =d # 현재 톱니바퀴 회전 저장

    turn_on(d,n)

    # 왼쪽 톱니바퀴 회전 체크
    # 현재 회전 하고 있는 톱니바퀴 3번과 왼쪽 톱니바퀴 7번 비교
    for li in range(n-1,0,-1):
        if gears[li][2] != gears[li+1][6]:
            # 반대 방향 회전
            directions[li] = -directions[li+1]
            turn_on(directions[li], li)

    # 오른쪽 톱니바퀴 회전 체크
    for ri in range(n+1, 5):
        if gears[ri][6] != gears[ri-1][2]   :
            directions[ri] = -directions[ri-1]
            turn_on(directions[ri],ri)



# 점수 확인
total = 0


for i in range(1,5):
    if gears[i][0] == '1':
        total += 2**(i-1)

print(total)







