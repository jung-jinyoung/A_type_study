import sys
sys.stdin = open('sample_input.txt','r')

# swea_2117_홈 방범 서비스
# 메모리 : 50,564 kb
# 실행시간 : 655 ms



T = int(input())
for tc in range(T):
    N,M = map(int,input().split())                      # NxN 마을 and 각 집당 M만큼 지불
    arr = [list(map(int,input().split()))  for _ in range(N)]
    max_cnt = 0                                         # 최대 집개수 저장용
    house =[]                                           # 집 위치 저장용
    for i in range(N):
        for j in range(N):
            if arr[i][j]==1:
                house.append((i,j))                     # 순회하면서 집 위치 append

    for i in range(N):                                  # 순회하며 현재 위치를 마름모 중앙을 생각하자
        for j in range(N):
            for k in range(1,2*N-2):                    # 방범 거리는 끝에서 끝까지 일 때 최대인 2 X (N-1)
                cost = k * k + (k - 1) * (k - 1)        # 각 거리별 비용 계산
                cnt = 0
                for x,y in house:                       # 집 좌표를 순회
                    if abs(x-i)+abs(y-j)<k: cnt+=1      # 현 위치에서 집까지 거리가 K보다 작으면 마음모 안에 존재 한다는 뜻.
                if  max_cnt<cnt and cnt*M - cost >= 0:  # 기존에 저장한 최대 집 수 보다 많고 금전적 손해 없으면
                    max_cnt = cnt                       # 최대 집 수 갱신

    print(f'#{1+tc} {max_cnt}')

