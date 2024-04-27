"""

<진행 방향>
1. g-1 세대의 드래곤 커브 생성
=> g-1 세대의 꼭짓점 == g세대 시작점
=> g-1 세대의 방향 저장 리스트 => 90도 회전 후 방향으로 업데이트 == g 세대 방향 리스트
=> 그래프에 표시

2. 모든 드래곤 커브 생성 후 그래프 조회
=> 2-1.꼭짓점 조회 (4방향 확인)
=> 2-2. 모든 4개의 좌표가 드래곤 커브 좌표이면 완료 리스트에 조회 후 저장
2-1~2-2 반복



"""

di = [0,-1,0,1]
dj = [1,0,-1,0]
op = [1,2,3,0] # 90도 회전 후 di,dj 인덱스

graph = [[0]* 101 for _ in range(101) ] # 좌표 저장이 아닌, 그래프 표시로 변경

N = int(input())

for _ in range(N):
    x,y,d,g = map(int,input().split()) # (x,y) 시작점에서 d방향으로 이동 후, 총 g세대의 드래곤 커브를 가진다.

    directions = [] # 이동해야할 방향 저장 리스트
    graph[x][y] = 1

    directions.append(d)

    # 드래곤 커브 생성을 위한 방향 리스트 저장
    for _ in range(g):
        # 현재 세대 드래곤 커브 생성

        for i in range(len(directions)-1, -1, -1):
            directions.append(op[directions[i]])

    # 드래곤 커브 만들기
    for i in range(len(directions)):
        x += di[directions[i]]
        y += dj[directions[i]]

        if x < 0 or x >= 101 or y < 0 or y >= 101: #범위가 벗어난다면
            continue
        graph[x][y] = 1

answer = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] == 1 and graph[i + 1][j] == 1 and graph[i][j + 1] == 1 and graph[i + 1][j + 1] == 1:
            answer += 1

print(answer)
