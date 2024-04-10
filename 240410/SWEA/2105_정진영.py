"""
임의의 한 카페에서 출발 -> 대각선 방향으로 이동
-> 사각형 모양을 그리며 다시 출발점으로 돌아옴

* 왔던 길로 다시 돌아올 수 없음
* 같은 디저트 종류를 팔 고 있는 카페 방문 X (숫자가 같은 카페)

접근 방법
1. 완전 탐색 : 갈 수 있는 대각선 방향 모두 탐색


"""


# 대각선 이동 델타
di = [1, 1, -1, -1]
dj = [1, -1, 1, -1]

def check(i,j,e): # 이동한 위치 저장 리스트 s, 디저트 저장 리스트 e
    global ans
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if 0<=ni<N and 0<=nj<N :
            if visited[ni][nj] == 1: # 다음 이동할 장소가 출발점이라면
                ans = max(ans,len(e)) # 값 비교
                return

            next = region[ni][nj]
            # 같은 종류의 디저트 카페를 방문하지 않았으면
            if not visited[ni][nj] and next not in e:
                visited[ni][nj] = visited[i][j] +1
                e.append(next)
                check(ni,nj,e)

                #초기화
                visited[ni][nj] = 0
                e.pop()


T = int(input())
for tc in range(1,T+1):
    N = int(input()) # 지역의 길이

    region = [list(map(int,input().split())) for _ in range(N)]

    ans = 0 # 먹을 수 있는 디저트의 수 초기화
    for i in range(N):
        for j in range(N):
            start = region[i][j]
            visited = [[0] * N for _ in range(N)]
            visited[i][j] = 1 # 시작
            check(i,j,[start])

    if not ans:
        print(f'#{tc} -1')
    else:

        print(f'#{tc} {ans}')
