# 그래서 몇 개의 줄을 바꿔야 성능 테스트를 통과하는지를 못 구하겠어!!

D, W, K = map(int, input().split())
film = [list(map(int, input().split()))for _ in range(D)]
minans = 10 ** 8

def count(film):
    # 탐색
    ans = 0             # K개 연속인 줄이 몇 개인가?
    for j in range(W):
        cnt = 1         # 줄마다 성능 테스트 K개 연속인지 확인
        for i in range(1,D):
            if film[i-1][j] == film[i][j]:  
                cnt += 1
            if  cnt == K:
                ans += 1 # 세로로 읽으면서 연속되는 특성이 K개가 되면 cnt += 1
                break    # 그 줄이 통과했으면 뒤엔 안 봐도 됨
    return ans

def dfs(k, film):
    global minans

    if count(film) == W:
        print()

    # 1. k번째 줄 안 바꿀 때
    count(film)

    # 2. k번째 줄 0 으로 바꿀 때
    tmp = film[k]
    film[k] = [0] * W
    count(film)
    film[k] = tmp
    
    # 3. k번째 줄 1 로 바꿀 때
    tmp = film[k]
    film[k] = [1] * W
    count(film)
    film[k] = tmp

    # 다음 단계로
    dfs(k+1, film)

dfs(0, film)
