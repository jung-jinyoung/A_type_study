"""
셀이 가질 수 있는 특성은 A, B
성능 검사 통과 :세로 방향에 대해서 동일한 특성의 셀들이 K개 이상 연속적으로 있는 경우
성능 검사 통과 못할 경우 : 약품 투입 => 가로 셀의 특성이 모두 해당 약품의 특성으로 변경
출력 : 성능 검사 통과를 위한 약품 투입의 횟수

약품 투입을 할 수 있는 셀들의 개수 : D (두께)
성능 검사를 해야하는 세로 행의 개수 : W(가로 크기)


접근 방법 : 완전 탐색 + DFS + 백트래킹
- 약물 A, B 넣을 경우 모두 탐색
- 최소 투입 회수보다 크면 가지치기

메모리 :  70,720 KB
시간 : 1,502 ms

"""

# 성능 검사 함수
def check():
    for j in range(W): # 모든 세로 셀들 확인
        cnt = 1
        for i in range(1,D):
            if film[i][j] == film[i-1][j]:
                cnt+=1
            else: # 다를 경우 초기화
                cnt =1
            # j 열 성능 검사 통과 여부
            if cnt >=K :
                break
        else: # K 개 이상이 아닐 경우
            return False
    return True

def dfs(i,c): # 현재 i 행에서의 카운트 c
    global min_value
    if c >=min_value : # 가지 치기
        return
    if i == D:
        if check(): # 성능 검사 통과 했을 경우
            min_value = min(min_value, c)
        return

    dfs(i+1,c) # 약물 투입 X

    # 약물 투입
    tmp = film[i][:] # 임시 저장
    film[i] = [0] * W # A 성분 투입
    dfs(i+1,c+1)
    film[i] = [1]*W # B 성분 투입
    dfs(i+1,c+1)

    #초기화
    film[i] = tmp


T = int(input())
for tc in range(1,T+1):
    D, W, K = map(int,input().split())
    #  보호 필름의 두께 D, 가로 크기 W, 합격 기준 K
    A, B = 0, 1
    film = [list(map(int,input().split())) for _ in range(D)]

    min_value = int(1e9) # 최소 투입 횟수 초기화

    if check(): # 이미 성능 검사 통과할 경우
        print(f'#{tc} 0')
    else:
        dfs(0,0)
        print(f'#{tc} {min_value}')