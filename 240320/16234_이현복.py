
'''
16234_인구 이동

메모리 : 125568KB
시간 : 1012ms
'''

def func(x,y):
    global result
    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ni, nj = x + di, y + dj
        if 0 <= ni < N and 0 <= nj < N and L<=abs(A[x][y]-A[ni][nj])<=R and union[ni][nj]==0:              
            union[ni][nj] = zone            # 국경 오픈한 나라들을 모두 같은 숫자로 union 배열에 표시
            result[0]+=1                    # 국경 닫은 이후 인원 수 변경을 위한 [개수,인구 합,[좌표들]]
            result[1]+=A[ni][nj]
            result[2].append((ni,nj))
            func(ni,nj)

N,L,R = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
while 1:
    cnt+=1
    zone = 1
    union=[[0]*N for _ in range(N)]
    stack = []
    for i in range(N):
        for j in range(N):
            if union[i][j] == 0:
                result = [0,0,[]]           #[개수,인구 합,[좌표들]]
                func(i,j)
                if result[0]:               # 받아온 배열의 0번 인덱스인 개수가 1이상이면
                    stack.append(result)    # 받아온 배열을 저장하는 stack 배열에 append
                    zone+=1                 # 다른 zone 표시를 위해 증가
    for area in stack:              # 각 연합별로 순회하며 인원 변경을 해주자
        people = area[1]//area[0]
        while area[2]: 
            x,y=area[2].pop()
            A[x][y]=people
    if union == [[0]*N for _ in range(N)]:
        cnt-=1
        break
print(cnt)
