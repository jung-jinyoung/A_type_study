import sys
sys.stdin = open('sample.txt','r')

# swea_5644_무선 충전
# 메모리 : 52,488 kb
# 실행시간 : 280 ms


delta=((0,0),(-1,0),(0,1),(1,0),(0,-1))                     # 문제에 따라서 움직이지 않는 경우 추가
T = int(input())
for tc in range(T):
    M,A = map(int,input().split())  # 총 이동 시간(M), BC의 개수(A)
    move_A = list(map(int, input().split()))
    move_B = list(map(int, input().split()))
    arr = [list(map(int,input().split())) for _ in range(A)]    # j,i,C,P
    power=0
    xa, ya, xb, yb = 1,1,10,10                              # 시작점이 각각 1,1 과 10,10 이다.
    t=0

    while t<=M:
        A_charge = []               # 이번 반복에서 A가 밟는 충전기의 충전파워 저장용
        B_charge = []               # 이번 반복에서 B가 밟는 충전기의 충전파워 저장용
        for idx in range(A):
            if abs(xa - arr[idx][1]) + abs(ya - arr[idx][0]) <= arr[idx][2]:    # 거리 계산 결과가 충전기 범위 내부 라면
                A_charge.append((arr[idx][3],idx))         # append를 (power,index) => 같은 파워인데 다른 충전기 일 때 분리용
            if abs(xb - arr[idx][1]) + abs(yb - arr[idx][0]) <= arr[idx][2]:
                B_charge.append((arr[idx][3],idx))
        A_charge.sort()                                     # 오름차순으로 정렬
        B_charge.sort()
        if A_charge and B_charge:
            if A_charge[-1]!=B_charge[-1]:                  # 밟은 가장 큰 충전기가 둘다 같지 않으면
                power+=(A_charge[-1][0]+B_charge[-1][0])
            else:                                           # 밟은 가장 큰 충전기가 같다
                if len(A_charge)==1 and len(B_charge)==1:   # 둘 다 하나씩 만 밟았으면 반반 해야지 뭐...
                    power += A_charge[-1][0]
                elif len(A_charge)==1:                      # A는 하나이고 B는 2개이상이면 B는 하나 작은 파워 충전기로 충전한다
                    power+=(A_charge[-1][0]+B_charge[-2][0])
                elif len(B_charge)==1:
                    power+=(A_charge[-2][0]+B_charge[-1][0])
                else:                                       # A,B 모두 2개이상의 충전기 밟았으면 합을 비교해서 큰거로 충전
                    power += max(A_charge[-1][0]+B_charge[-2][0],A_charge[-2][0]+B_charge[-1][0])
        elif A_charge:              # A만 충전하는 경우
            power+= A_charge[-1][0]
        elif B_charge:              # B만 충전하는 경우
            power+= B_charge[-1][0]

        if t==M:                    # 종료 조건
            break
        xa, ya, xb, yb = xa+delta[move_A[t]][0],ya+delta[move_A[t]][1],xb+delta[move_B[t]][0],yb+delta[move_B[t]][1]
        t+=1
    print(f'#{1+tc} {power}')