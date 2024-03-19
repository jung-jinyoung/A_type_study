# 치킨 배달

def combination(i,cnt):
    global ans
    if cnt == M:
        tmp = 0
        for s in range(len(home)):
            hi, hj = home[s]
            min_distance = 100
            for k in range(len(chicken)):
                ci, cj = chicken[k]
                if visited[k]:
                    distance = abs(hi-ci) + abs(hj-cj)
                    if min_distance > distance:
                        min_distance = distance
            
            tmp += min_distance
        if ans > tmp:
            ans = tmp
        return
    if i == len(chicken):
        return
    
    visited[i] = 1
    combination(i+1,cnt+1)
    visited[i] = 0
    combination(i+1,cnt)

N, M = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

chicken = []
home = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chicken.append([i,j])
        elif arr[i][j] == 1:
            home.append([i,j])


ans = 10**9
visited = [0]*len(chicken)
combination(0,0)

print(ans)

