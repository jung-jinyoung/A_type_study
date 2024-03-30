"""
메모리 : 31120KB
시간 : 52ms

"""
def bfs(s, N, G):
    q = [s] # 큐 생성
    v = [0]*(N+1) # .방문 리스트 생성
    v[s] = 1 # 방문 표시
    cnt = 0
    while q:
        t = q.pop(0)
        cnt += 1
        for i in info[t][1:]:
            if i in G and v[i] == 0:
                q.append(i)
                v[i] = 1
    if len(G)==cnt:
        return 1
    else:
        return 0

N = int(input())
peoples = [0] + list(map(int, input().split()))   # 각 도시들의 인구
info = [[]] # 각 도시의 연결 정보
for _ in range(N):
    info.append(list(map(int, input().split())))

minV = 1000 # 인구 차이 최솟값 초기화

for i in range(1,(1<<N)//2): ## 절반만 확인해도 가능
    A = []  # 선거구 A, B 설정
    B = []
    pa = 0  # 선거구 A, B 인구 합 초기화
    pb = 0
    for j in range(N):
        if i&(1<<j):    # j번 도시의 소속 선거구
            A.append(j+1)
            pa += peoples[j+1]
        else:
            B.append(j+1)
            pb += peoples[j+1]
    if bfs(A[0], N, A) and bfs(B[0], N, B): # 두 선거구 모두가 연결되어 있는지 bfs로 확인
        if minV > abs(pa-pb): # 현재 인구 차이 비교
            minV = abs(pa-pb)
if minV == 1000: # 인구 차이가 업데이트 되지 않았다면
    minV = -1
print(minV)