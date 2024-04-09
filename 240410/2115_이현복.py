import sys
sys.stdin = open('sample_input.txt','r')


'''
2115_벌꿀채취
237 ms
52,456 kb
'''

def dfs(level,sumv):
    global res
    if level == 2:          # 2명이니까 종료는 2일때
        if res < sumv:      # 더 클때 갱신
            res = sumv
        return
    for i in range(N):
        for j in range(nn):
            for l in range(j-M,j+M):
                if 0<=l<nn:                 # 앞뒤로 겹치는 구간
                    if visited[i][l]!=0:    # 방문 했으면 불가한 경우니까 break
                        break
            else:                           # for-else로 앞뒤 곂치는 구간 없다
                if visited[i][j] == 0:      # 방문한 적 없으면
                    visited[i][j] = 1       # 방문 표시
                    dfs(level+1,sumv+data[i][j])
                    visited[i][j] = 0       # 방문 취소

T = int(input())
for tc in range(T):
    N,M,C = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    nn = N-M+1                              # M개씩 그룹화 했을때 수익을 2중 리스트로 만듬
    data = [[0]*nn for _ in range(N)]
    for i in range(N):
        for j in range(N - M + 1):
            temp = []
            for k in range(M):
                temp.append(arr[i][j+k])        # M개를 append
            if sum(temp)<=C:                    # M개의 합을 C와 비교
                data[i][j]=sum(map(lambda x:x**2,temp))     # 각 원소 제곱하고 합친다
            else:
                comp = 0
                for x in range(1<<M):       # 조합으로 합이 C보다 작고 제곱 합이 최대 인거 찾는다.
                    stack = []
                    for y in range(M):
                        if x&(1<<y):
                            stack.append(temp[y])
                    if sum(stack)<=C:
                        comp = max(comp,sum(map(lambda x:x**2,stack)))
                data[i][j] = comp
    visited = [[0]*nn for _ in range(N)]
    res=0
    dfs(0,0)
    print(f'#{tc+1} {res}')