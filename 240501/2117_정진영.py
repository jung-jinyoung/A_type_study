"""

접근 방법 : 완전 탐색

보험 회사의 이익 : M*(영역 안의 집 개수) - 운영 비용
운영 비용 = K**2 + (K-1)**2
손해를 보지 않으면서 가장 많은 집들에 제공하는 서비스 영역


K를 하나씩 늘리면서 완전 탐색
1) 이익 < 0 : M * (영역 안의 집 개수) < 운영 비용
2) 모두 다 돌았을 때 손해를 보지 않았으면 ans와 비교 : max(ans,m)

메모리 : 52708 kb
시간 : 1470ms
"""
import sys

sys.stdin = open('input.in','r')
def find(k): # 현재 탐색 범위는 k
    global max_ans
    cost = k**2 + (k-1)**2
    for i in range(N):
        for j in range(N):
            # 현재 중심점(i,j)에서 집 카운트 초기화
            count = 0

            # 마름모 영역 탐색 범위 설정
            for x in range(i-k+1,i+k):
                for y in range(j-k+1,j+k):
                    # 범위를 벗어 나지 않고 해당 위치에 집이 있을 경우
                    if 0<=x<N and 0<=y<N and city[x][y]==1:
                        # 현재 위치와 중심점까지 거리 비교
                        distance = abs(i-x)+abs(j-y)
                        if distance < k :
                            count +=1
            profit = (M*count) - cost
            if profit >=0 :
                max_ans = max(max_ans,count)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]

    max_ans = 0 # 초기화
    check = 0 # 손해 발생하지 않고 업데이트 여부
    for k in range(1,N+2):
        find(k)

    print(f'#{tc} {max_ans}')


