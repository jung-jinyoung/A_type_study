"""

<진행 방향>
1. g-1 세대의 드래곤 커브 생성
=> g-1 세대의 꼭짓점 == g세대 시작점
=> g-1 세대의 방향 저장 리스트 => 90도 회전 후 방향으로 업데이트 == g 세대 방향 리스트

2. 모든 드래곤 커브 생성 후 꼭짓점 좌표 저장 리스트 조회
=> 2-1.꼭짓점 조회 (4방향 확인)
=> 2-2. 모든 4개의 좌표가 드래곤 커브 좌표이면 완료 리스트에 조회 후 저장
2-1~2-2 반복



"""

di = [0,-1,0,1]
dj = [1,0,-1,0]
op = [1,2,3,0] # 90도 회전 후 di,dj 인덱스

N = int(input())
curves = [list(map(int,input().split())) for _ in range(N)] # 시작 커브들 저장

positions = [] # 드래곤 커브들이 지나간 좌표 저장 리스트
result = [] # 완성된 드래곤 커브의 꼭짓점 좌표 저장 리스트

for curve in curves :
    x,y,d,g = curve # (x,y) 시작점에서 d방향으로 이동 후, 총 g세대의 드래곤 커브를 가진다.

    directions = [] # 이동해야할 방향 저장 리스트

    if (x,y) not in positions:
        positions.append((y,x))

    si,sj = y,x # 시작점 지정
    directions.append(d)

    # 0세대 드래곤 커브 생성

    ni = si + di[d]
    nj = sj + dj[d]

    if 0 <= ni < 100 and 0 <= nj < 100:  # 범위를 벗어나지 않으면 이동
        # 좌표 확인 후 저장
        if (ni, nj) not in positions:
            positions.append((ni, nj))
        si, sj = ni, nj  # 다음 세대의 시작점 업데이트



    # 1세대 이후 드래곤 커브 생성
    for _ in range(g):
        # 현재 세대 드래곤 커브 생성
        L = len(directions)
        # 이동
        for i in range(L):
            now = directions[i]
            ni = si + di[op[now]]
            nj = sj + dj[op[now]]
            directions.append(op[now])
            if 0 <= ni < 101 and 0 <= nj < 101:  # 범위를 벗어나지 않으면 이동
                # 좌표 확인 후 저장
                if (ni, nj) not in positions:
                    positions.append((ni, nj))
                si, sj = ni, nj  # 다음 세대의 시작점 업데이트


        # 다음 세대 이동 리스트 업데이트
        next_directions = []
        for i in range(len(directions)):
            next_directions.append(op[directions[i]])
        directions = next_directions

# 모든 드래곤 커브 생성 후 꼭짓점 좌표 저장 리스트 조회
for i in range(100):
    for j in range(100):
        # 각 꼭짓점을 확인하여 주어진 조건에 맞는 드래곤 커브인지 판별
        if (i, j) in positions and (i + 1, j) in positions and (i, j + 1) in positions and (
        i + 1, j + 1) in positions:
            # 주어진 조건에 맞는 드래곤 커브인 경우, 결과 리스트에 추가
            result.append((i, j))

# 결과 출력
print(len(result))
