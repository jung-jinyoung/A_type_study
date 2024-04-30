# 등산로 조성

'''
구글링 참고함 .. 
봉우리는 가장 높은 곳에서부터 시작
높은 지형에서 낮은 지형으로, 가로 또는 세로 연결
한 곳에 한해서 k 깊이 만큼 지형을 깎을 수 있음
가장 긴 등산로 찾기
'''

T = int(input())
for tc in range(1, T+1):
    # n : 지도 크기 k : 최대 공사 가능 깊이
    n,k = map(int,input().split())
    # 지도
    board = [list(map(int,input().split())) for _ in range(n)]
    # 가장 높은 봉우리의 위치를 저장할 리스트 만들기
    peaks = []
    max_peak = max(map(max,board))
    for i in range(n):
        for j in range(n):
            if board[i][j]==max_peak:
                peaks.append([i,j])

    answer=[0]
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    def dfs(x,y,cnt):
        # 가장 긴 등산로의 길이로 업데이트
        answer[0]=max(answer[0],cnt)
        for i in range(4):
            cx=x+dx[i]
            cy=y+dy[i]
            # 범위 내에 있고 현재의 높이보다 낮고 방문한 적이 없을 때
            if 0<=cx<n and 0<=cy<n and board[cx][cy]<board[x][y] and visited[cx][cy]==0:
                # 방문 처리
                visited[cx][cy]=1
                dfs(cx,cy,cnt+1)
                # 방문 처리 원상복구
                visited[cx][cy]=0
    # 지도 순회 
    for i in range(n):
        for j in range(n):
            # 깎을 수 있는 깊이의 모든 경우 탐색
            for deep in range(k):
                deep+=1
                # 깎았을 때의 높이가 0 보다 클때만 깎음
                if board[i][j]-deep>=0:
                    board[i][j]-=deep
                    for peak in peaks:
                        # 방문 표시할 배열 생성
                        visited=[[0 for _ in range(n)] for _ in range(n)]
                        # 방문표시
                        visited[peak[0]][peak[1]]=1
                        dfs(peak[0],peak[1],0)
                    # dfs 순회 끝났을 경우 높이 다시 원상복구
                    board[i][j]+=deep
    # cnt 를 0 부터 시작하므로 answer 에 +1
    print(f'#{tc} {answer[0]+1}')