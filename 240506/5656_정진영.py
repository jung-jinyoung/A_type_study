"""

재귀 (중복순열)로 푸는 중 .. .
현재 런타임 에러 ㅠ
"""


def shot(cnt,arr,broken_total): # 남은 횟수 cnt, 영역 arr에서 부순 벽돌의 개수 total
    global total, ans
    # 벽돌을 다 깨면 return
    if total == broken_total:
        ans = total
        return
    # 구술을 다 쏘면 return
    if cnt == 0:
        if broken_total > ans:
            ans = broken_total
            return

    for i in range(W):
        tmp = [ row[:] for row in arr] # 게임판 전체를 카피
        stack = []
        blocks = 0 # 벽돌 초기값

        for j in range(H):
            if tmp[j][i]:
                stack.append((j,i))
                break
        while stack :
            x, y = stack.pop()
            if not tmp[x][y]:
                continue
            blocks+=1
            for _ in range(tmp[x][y]-1):
                for dx, dy in [(-1,0),(0,1),(1,0),(0,-1)]:
                    nx = x + dx
                    ny = y + dy
                    if 0<=nx<H and 0<=ny<W:
                        stack.append(nx,ny)
            tmp[x][y] = 0 # 제거
        # 벽돌 내리기
        for y in range(W):
            idx = H-1
            for x in range(H-1,-1,-1):
                if not tmp[x][y]:
                    continue
                tmp[idx][y], tmp[x][y] = tmp[x][y], tmp[idx][y]
                idx -=1
        shot(cnt-1,tmp,broken_total + blocks )



T = int(input())
for tc in range(1,T+1):
    N, W ,H = map(int,input().split())
    # H*W 영역에 있는 벽돌들에 N번 구슬을 쏜다.
    arr = [list(map(int,input().split())) for _ in range(H)]
    total = 0 # 전체 블록의 개수 초기화
    # 총 벽돌 개수 세기
    for i in range(H):
        for j in range(W):
            if arr[i][j]:
                total += 1
    ans = 0
    shot(N,arr,0)
    print(f'#{tc} {total-ans}')
