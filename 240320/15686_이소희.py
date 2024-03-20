'''
시간 900 ms, 메모리 31120 KB
위에도 좀 복잡하고
최솟값 구하는 부분이 진짜 번거로워서
시간초과 날 줄 알았는데 통과해서 기뻐
'''
# 남겨둘 치킨집 조합을 만드는 함수
def com(lst, prev):
    if len(lst) == M:
        combilst.append(lst[:])
        return
    for i in range(len(index)):
        if visited[i] == 0 and index[i] > prev:
            visited[i] = 1
            com(lst + [index[i]], index[i])
            visited[i] = 0
    
N, M = map(int, input().split())
town = [list(map(int, input().split())) for _ in range(N)]
# 치킨집과 집의 좌표 저장하기
kyochon = []
home = []
for i in range(N):
    for j in range(N):
        if town[i][j] == 2:
            kyochon.append((i,j))
        elif town[i][j] == 1:
            home.append((i,j))
# print(kyochon)

# 조합을 만들어서 저장해둘 리스트
combilst = []
index = [i for i in range(len(kyochon))]
visited = [0] * len(kyochon)
com([],-1)
# print(combilst)

# 최소값 구하는 과정
result = 50 * 10 ** 7
for p in range(len(combilst)):
    distance = 0
    for r in range(len(home)):
        h_r, h_c = home[r][0], home[r][1]
        min_dist = 50 * 10 ** 7
        for q in range(M):
            chi_r, chi_c = kyochon[combilst[p][q]][0], kyochon[combilst[p][q]][1]
            # 집에서 각 치킨집까지 거리를 구함
            tmp_dist = abs(chi_r - h_r) + abs(chi_c - h_c)
            min_dist = min(min_dist, tmp_dist) # 그리고 비교함
        # 그걸 또 distance에 담아서 최종적으로 비교할 것임
        distance += min_dist
    result = min(result, distance)
# 끝
print(result)
