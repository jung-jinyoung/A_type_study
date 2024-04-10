'''
정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점의 번호 V
M개의 줄에 걸쳐 연결하는 두 정점의 번호
'''
from collections import deque
def dfs(v):
    # 현재 노드
    now = v
    d_visited[now] = 1 # 방문처리
    print(now, end = ' ')
    # 현재에서 갈 수 있는 노드 목록
    node[now].sort() # 정점 번호가 작은 것 먼저 방문
    for next in node[now]:
        if not d_visited[next]: # 다음 목록에 있는 노드를 방문한 적이 없다면
            d_visited[next] = 1
            dfs(next)
    
def bfs(v):
    q = deque([])
    q.append(v)
    while q:
        now = q.popleft()
        b_visited[now] = 1 # 방문처리
        print(now, end = ' ')
        node[now].sort() # 정점 번호가 작은 것 먼저 방문
        for next in node[now]:
            if b_visited[next] == 0: # 다음을 방문한 적이 없다면
                q.append(next)
                b_visited[next] = 1 # 방문처리

N, M, V = map(int, input().split())
node = [[]  for _ in range(N+1)]
d_visited = [0] * (N+1) # dfs에서 사용하는 visited
b_visited = [0] * (N+1) # bfs에서 사용하는 visited

for _ in range(M):
    s, e = map(int, input().split())
    # 간선은 양방향
    node[s].append(e)
    node[e].append(s)

dfs(V)
print()
bfs(V)