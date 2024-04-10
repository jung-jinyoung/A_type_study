import sys
sys.stdin = open('sample_input.txt','r')

'''
2383_점심 식사시간
52,756 kb
220 ms

조합을 만들고 각 경우를 함수에 넣어서 처리
함수 내부 순서가 중요
for문 하나로 계단 내,외부 한번에 돌리면 순회 순서에 따라 들어가야 하는데 들어가지 못하는 상황 발생
'''
def fff():
    cnt =0
    fin = 0
    ing=[0,0]
    while fin != (len(goto)):
        cnt+=1
        for i in range(len(goto)):                          # 계단에 있는 친구들 먼저 순회로 돌린다
            if goto[i][0] == (-1) * stair[goto[i][1]][2]:   # 마지막 계단이면...
                fin += 1
                ing[goto[i][1]] -= 1
                goto[i][0] = 30                             # 식사중~
            elif goto[i][0]<0:                              # 계단 하나 내려간다
                goto[i][0] -= 1

        for i in range(len(goto)):                          # 계단 밖 친구들 이동
            if goto[i][0] == 30:                            # 이미 내려간 친구는 pass
                continue
            elif goto[i][0]==0:                             # 계단 도착한 친구
                if ing[goto[i][1]]<3:                       # 계단에 3명 미만이면 입장
                    ing[goto[i][1]]+=1
                    goto[i][0] -= 1
            elif goto[i][0]>=0:                             # 아직 이동중
                goto[i][0]-=1
    return cnt

T=int(input())
for tc in range(T):
    N=int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    people = []
    stair = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]==1: people.append([i,j])           # 사람 위치 체크
            elif arr[i][j]>1:
                stair.append((i,j,arr[i][j]))               # 계단 위치와 계단 내려가는 시간 체크
    for idx in range(len(people)):
        distance1 = abs(stair[0][0]-people[idx][0]) + abs(stair[0][1] - people[idx][1])
        distance2 = abs(stair[1][0] - people[idx][0]) + abs(stair[1][1] - people[idx][1])
        people[idx][0],people[idx][1] = distance1,distance2 # 결국 people은 [계단1까지 거리, 계단2까지 거리 ]로 덮음

    res = 10 * 20 * 10                  # res = 최대 인원 X 최대 이동 시간 X 최대 계단 내려가는 시간
    for i in range(1<<len(people)):
        case = bin(i)[2:]
        diff = len(people) - len(case)
        if diff:
            case='0'*diff+bin(i)[2:]
        goto=[0]*len(people)
        for k in range(len(people)):
            goto[k]=[people[k][int(case[k])],int(case[k])]       # 어떤 계단으로?  조합! [거리,계단번호]
        res = min(res,fff())
    print(f'#{tc+1} {res}')