def dfs(level,sumv):
    global res
    if level == 2:
        if res < sumv:
            res = sumv
        return
    for i in range(N):
        for j in range(nn):
            for l in range(j-M,j+M):
                if 0<=l<nn:
                    if visited[i][l]!=0: break
            else:
                if visited[i][j] == 0:
                    visited[i][j] = 1
                    dfs(level+1,sumv+data[i][j])
                    visited[i][j] = 0


T = int(input())
for tc in range(T):
    N,M,C = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    nn = N-M+1
    data = [[0]*nn for _ in range(N)]
    for i in range(N):
        for j in range(N - M + 1):
            temp = []
            for k in range(M):
                temp.append(arr[i][j+k])
            if sum(temp)<=C:
                data[i][j]=sum(map(lambda x:x**2,temp))
            else:
                comp = 0
                for x in range(1<<M):
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