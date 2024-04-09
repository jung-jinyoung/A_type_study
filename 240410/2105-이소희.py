'''
메모리 85344 KB, 실행시간 2157 ms
'''
di = [1, 1, -1, -1, 1]
dj = [-1, 1, 1, -1, -1]

def route(t, i, j, tried):
    global result
    # tried : 이미 먹은 디저트 종류 목록
    if t > 3:
        return
    if t == 3 and (i, j) == (si, sj):
        # 처음으로 돌아온 동선 중에, 먹을 수 있는 디저트 종류가 가장 많은 경우
        result = max(result, len(tried))
        return
    
    for k in range(t, t+2):
        ni, nj = i + di[k], j + dj[k]
        # 범위 내, 방문한 적 없음, 디저트 종류가 이전과 다르면
        if 0 <= ni < N and 0 <= nj < N and cafe[ni][nj] not in tried:
            tried.append(cafe[ni][nj])
            # 시간 초과쓰
            # route(t, ni, nj, tried) # k 가 t일 때랑
            # route(t+1, ni, nj, tried) # k 가 t+1 일 때
            route(k, ni, nj, tried)
            tried.pop()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = -1
    cafe = [list(map(int, input().split()))for _ in range(N)]
    # 왼쪽 아래 대각선으로 이동하려면 j 범위가 1부터 시작해야 하고
    # 사각형을 그리고 돌아오려면 i가 0부터 N-2 범위내에 있어야 함
    for si in range(N-2):
        for sj in range(1, N-1):
            route(0, si, sj, [])
    print(f'#{tc} {result}')

