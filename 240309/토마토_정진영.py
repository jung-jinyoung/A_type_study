from collections import deque

def finding_tomato(box):
    finding = deque()
    # 상자를 열었을 때 현재 익은 토마토 찾기
    for i in range(N):
        for j in range(M):
            if box[i][j] == '1':
                finding.append((i, j))
    return finding


M, N = map(int,input().split())
# M*N 배열의 상자 크기
box = [input().split() for _ in range(N)]

# 현재 토마토들이 담겨있는 상자
q = finding_tomato(box)

visited =[[0] * M for _ in range(N)] # 방문 횟수 저장 리스트

max_date = 0

while q:
    i, j = q.popleft()

    for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        ni = i + di
        nj = j + dj

        if 0 <= ni < N and 0 <= nj < M and box[ni][nj] == '0':
            box[ni][nj] = '1'
            q.append((ni, nj))
            visited[ni][nj] = visited[i][j] + 1

            if max_date < visited[ni][nj]:
                max_date = visited[ni][nj]

# 익지 않은 토마토 점검
for i in range(N):
    for j in range(M):
        if box[i][j] == '0':
            print(-1)
            exit()
print(max_date)