"""
접근 : 완전 탐색 + dfs

49개에서 fail..
=> 디버깅 : 코어를 연결하지 않고 넘어가는 경우를 추가하지 않았음
=> 해결!

시간 : 1192ms
메모리 : 65060kb

"""

dx = [0, 1, 0, -1]  # 상하좌우 이동을 위한 리스트
dy = [1, 0, -1, 0]


def is_valid(x, y, direction):
    nx, ny = x, y
    while True:
        nx += dx[direction]
        ny += dy[direction]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            return True  # 전선이 범위를 벗어나면 유효
        if board[nx][ny] != 0:
            return False  # 전선이나 다른 프로세서를 만나면 유효하지 않음


def connect_wire(x, y, direction, connected):
    nx, ny = x, y
    count = 0
    while True:
        nx += dx[direction]
        ny += dy[direction]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            return count, connected  # 전선이 범위를 벗어나면 연결된 프로세서 개수와 전선 길이 반환
        board[nx][ny] = connected
        count += 1


def dfs(idx, connected_count, wire_length):
    global max_connected_count, min_wire_length

    if idx == len(processors):
        if connected_count > max_connected_count:
            max_connected_count = connected_count
            min_wire_length = wire_length
        elif connected_count == max_connected_count:
            if wire_length < min_wire_length:
                min_wire_length = wire_length
        return

    x, y = processors[idx]

    # 코어를 연결하지 않고 다음 코어로 넘어가는 경우
    dfs(idx+1, connected_count, wire_length)
    for direction in range(4):
        if is_valid(x, y, direction):
            count, connected = connect_wire(x, y, direction, idx + 1)

            # 전선을 연결할 수 있는 경우
            dfs(idx + 1, connected_count + 1, wire_length + count)

            # 되돌리기
            nx, ny = x, y
            for _ in range(count):
                nx += dx[direction]
                ny += dy[direction]
                board[nx][ny] = 0



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    processors = []

    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if board[i][j] == 1:
                processors.append((i, j))

    max_connected_count = 0
    min_wire_length = int(1e9)

    dfs(0, 0, 0)

    print(f'#{tc} {min_wire_length}')
