import sys
sys.stdin = open('sample_input.txt','r')


'''



'''
road=((1,1),(-1,1),(-1,-1),(1,-1))

def dfs(x,y,dir,visited,todo,static):
    global res
    if dir ==4:
        # if visited.count(1) == 10:
        #     for i in range(len(visited)):
        #         if visited[i]: print(i,end=" ")

        # print(static,visited.count(1),visited)
        res = max(res, visited.count(1))
        return
    if dir < 2:
        # for i in range(1,N-1):
        ni,nj = x+road[dir][0],y+road[dir][1]
        if 0<=ni<N and 0<=nj<N and not visited[arr[ni][nj]]:
            # print(ni,nj)
            visited[arr[ni][nj]]=1
            todo[dir]+=1
            dfs(ni, nj, dir, visited,todo,static)
            dfs(ni, nj, dir+1, visited,todo,static)
            return
        else:
            return
    else:
        # for i in range(1,N-1):
        # if 1:
        ni,nj = x+road[dir][0],y+road[dir][1]
        if 0<=ni<N and 0<=nj<N and (visited[arr[ni][nj]]==0 or visited[arr[ni][nj]]==10):
            # print(ni, nj)
            visited[arr[ni][nj]]=1
            todo[dir-2]-=1
            if todo[dir-2]==0:
                dfs(ni, nj, dir + 1, visited,todo,static)
            else:
                dfs(ni, nj, dir, visited,todo,static)
        else:
            return




T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    if 1:
        res = -1
        for i in range(1,N-1):
            for j in range(N-2):
                check=[0]*101
                check[arr[i][j]]=10
                dfs(i,j,0,check,[0,0],[0,0])
        # check=[0]*101
        # check[arr[1][2]]=10
        # dfs(1,2,0,check,[0,0])
        print(f'#{1+tc} {res}')