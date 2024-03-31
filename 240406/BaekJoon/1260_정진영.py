"""
DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력 ( 없으면 중단 )
조건 : 인접 정점의 번호가 더 작은 것 부터 방문

시간 : 68ms (Python3)
메모리 : 32236KB
"""
import sys


input = sys.stdin.readline

N, M, V = map(int,input().split())
# 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점의 번호 V

adj = [[] for _ in range(N+1)]
for _ in range(M):
    node1, node2 = map(int,input().split())
    adj[node1].append(node2)
    adj[node2].append(node1)

# 각 연결 노드 정렬
for nodes in adj:
    nodes.sort()

visited1 = [0] * (N+1) # dfs 방문 저장 리스트
visited2 = [0] * (N+1) # bfs 방문 저장 리스트
print(adj)
def dfs(start):
    visited1[start] =1  # 방문 표시
    print(start,end = ' ')
    for next in adj[start]:
        if not visited1[next]:
            dfs(next)

dfs(V)
print()
def bfs(start):
    q = [] # 큐 생성
    visited2[start] = 1 # 방문 표시
    q.append(start) # 큐 시작 노드 저장
    while q :
        now = q.pop(0) # 현재 노드
        print(now, end = ' ') # 출력
        for next in adj[now]:
            if not visited2[next]:
                visited2[next]=1
                q.append(next)

bfs(V)