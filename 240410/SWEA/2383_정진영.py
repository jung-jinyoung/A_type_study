
from collections import deque
def find():
    for i in range(N):
        for j in range(N):
            if room[i][j]:
                if room[i][j]==1: # 사람이 위치해 있으면
                    person.append((i,j))
                else: # 계단실이라면
                    stairs.append((i,j))

def check(stairsN,index): # index번 째의 계단실
    if not stairsN: # 계단실을 사용하지 않을 경우
        return 0

    sr, sc = stairs[index][0], stairs[index][1]  # 계단실 위치
    K = room[sr][sc] # 계단실 길이


    now = [] # 현재 계단실 사용 상태
    # 현재 위치에서 계단실 까지의 거리 구하기
    for i in range(len(stairsN)):
        pr, pc = person[i]
        distance = abs(sr-pr) + abs(sc-pc) # 계단실 까지의 거리
        now.append([i, distance])
    now.sort(key = lambda x: x[1]) # 거리 순 정렬

    total = 0
    using = deque() # 현재 사용중인 계단실 상황 (더미 생성)
    # 사용중이라면 사용중인 사람의 인덱스가 들어감
    cnt = 0
    used = [0]*len(stairsN) # 계단실 사용 확인

    while cnt < K:
        total+=1

        # 계단실 확인
        while using:
            p, c = using.popleft()
            c+=1
            if c == K :# 계단실을 다 내려 왔다면 pop
                cnt+=1
                continue
            using.append([p,c]) # 다시 계단실 사용 추가


        for turn in range(len(stairsN)):
            if now[turn][1]: # 아직 계단실에 도착 하지 못 했을 경우
                now[turn][1] -=1

            if now[turn][1] == 0: # 계단실 도착
                if not used[turn]: #아직 계단실을 사용하지 못했다면 계단실 확인
                    if len(using) == K: # 계단실을 모두가 사용하고 있다면
                        continue
                    using.append([turn,1])

    return total




def dfs(i,stairs1): # i번째 사람 탐색, 계단실 1 사용 사람 저장 리스트 s
    global ans
    if i ==L:
        stairs2 = [j for j in range(L) if j not in stairs1]
        time1 = check(stairs1,0) # 시간 구하기
        time2 = check(stairs2,1)

        time = max(time1,time2) # 총 시간 구하기
        ans = min(ans,time) # 최소 시간 구하기
        return

    dfs(i+1,stairs1+[i]) # 계단실 1 사용
    dfs(i+1,stairs1) # 계단실 1 사용 X


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    person = []  # 행의 값이 작은 순서대로 저장
    stairs = []  # 계단실은 총 두개

    find() # 계단실과 현재 사람의 위치 찾기
    L = len(person) # 사람들 수

    ans = int(1e9)  # 최소값 초기화
    dfs(0, [])

    print(f'#{tc} {ans}')
