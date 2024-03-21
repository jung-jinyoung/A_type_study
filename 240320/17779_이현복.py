'''
17779번_게리맨더링 2 
시간 : 320ms
메모리 : 112052KB
'''

def draw(x,y,d1,d2):
    cnt = [0]*5                             # 각 지역 인원 저장용
    arr = [[0]*(N+1) for _ in range(N+1)]   # 지역 번호 적는용 배열

    left=right=y                            # 5번 지역 부터 구하자
    left_end=right_end=1
    for i in range(x,x+d1+d2+1):            # 5번 지역의 행을 순회
        for j in range(left,right+1):       # 5번 지역의 열을 순회
            arr[i][j]=5                     # 지역 표시
            cnt[4]+=A[i-1][j-1]             # 각 자리에 저장된 인원수를 cnt에 추가
        if left==y-d1: left_end*=(-1)       # 좌측의 꺾는 지점
        if right==y+d2: right_end*=(-1)     # 우측의 꺾는 지점
        left-=left_end
        right+=right_end

    for i in range(1,N+1):                  # 1~4번 지역 구하자
        for j in range(1,N+1):
            if i<x+d1 and j<=y:region=1
            elif i<=x+d2 and j>y: region=2
            elif i>=x+d1 and j<y-d1+d2: region=3
            else:region=4
            if arr[i][j]==0:
                cnt[region-1]+=A[i-1][j-1]
                arr[i][j] = region
    return max(cnt)-min(cnt)

res=0
N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]

for X in range(N):     # 각각 값의 범위를 정해줬었는데 오류나서 if문에 조건을 넣어서 해결
    for Y in range(N):
        for D1 in range(1,N):
            for D2 in range(1,N):
                if 1<=X<X+D1+D2<=N and 1<=Y-D1<Y<Y+D2<=N:
                    if res:                     # 비교해서 작은거만 취한다
                        res = min(res,draw(X,Y,D1,D2))
                    else:                       # 처음에 저장용
                        res = draw(X,Y,D1,D2)
print(res)