# DFS와 BFS

'''
N : 정점의 개수
M : 간선의 개수
V : 탐색을 시작할 정점의 번호
정점번호가 작은 것을 먼저 방문
간선은 양방향
'''

'''
노드의 인덱스에 연결된 노드 저장
각 노드를 오름차순 정렬
방문 처리할 배열
'''
def dfs(c):
    # 시작 노드
    ans_dfs.append(c)
    v[c] = 1

    for n in adj[c]:
        if not v[n]:
            # 방문하지 않은 노드인 경우
            dfs(n)

def bfs(s):
    q = []
    q.append(s)
    ans_bfs.append(s)
    v[s] = 1

    while q:
        c = q.pop(0)
        for n in adj[c]:
            if not v[n]:
                q.append(n)
                ans_bfs.append(n)
                v[n] = 1

N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    # 양방향이므로 양쪽 다 넣어줌
    adj[s].append(e)
    adj[e].append(s)

# 오름차순 정렬
for i in range(1,N+1):
    adj[i].sort()

# visited 
v = [0]*(N+1)
ans_dfs = []
dfs(V)

v = [0]*(N+1)
ans_bfs = []
bfs(V)

print(*ans_dfs)
print(*ans_bfs)