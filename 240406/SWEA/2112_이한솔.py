# 보호필름

'''
W : 막을 구성하는 셀의 개수
D : 쌓인 막의 수 
K : 합격 기준

필름의 성능은 셀들의 특성의 배치 형태에 따라 달라짐
단면의 모든 세로 방향에 대해서 동일한 특성이 
K개 이상 연속적으로 있는 경우에만 성능검사 통과
약품처리 시 막을 구성하는 모든 셀이 약품과 같은 특성으로 변경

약품 투입 횟수의 최소값 출력
'''

'''
메모리 : 62492kb 시간 : 2951ms 
너무 어려워서 dfs 함수 짤 때 약간의 구글링 참고
'''

# 성능검사
def test():
    for i in range(W):
        # 연속된 개수 측정을 위해 
        flag = film[0][i]
        check = 0
        for j in range(D):
            # 세로 방향에 같은 특성을 가진 셀이 있는 경우
            if flag == film[j][i]:
                # +1
                check += 1
            # 아닌 경우
            else:
                # 기준을 변경 (a<->b)
                flag = film[j][i]
                check = 1
            # 성능 기준인 K 와 같거나 커지면
            if check >= K:
                break
        # K보다 작으면
        if check < K:
            return False
    return True

def dfs(cnt, idx):
    global min_cnt
    # 초기 상태에서 성능 체크
    # 초기 상태에서 이미 성능이 적합 할 경우를 위한 가지치기
    if test():
        min_cnt = min(cnt,min_cnt)
        return 
    
    # min_cnt 보다 커지면, 가지치기
    if cnt >= min_cnt:
        return
    
    for i in range(idx+1,D):
        ori_film = film[i][:]
        for j in range(W):
            # 특성을 B로 변경하는 경우
            film[i][j] = 1
        dfs(cnt+1,i)

        for j in range(W):
            # 특성을 A로 변경하는 경우
            film[i][j] = 0
        dfs(cnt+1,i)

        for j in range(W):
            # 원상복귀
            film[i][j] = ori_film[j]

T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    min_cnt = D+1
    dfs(0,-1)
    print(f'#{tc} {min_cnt}')