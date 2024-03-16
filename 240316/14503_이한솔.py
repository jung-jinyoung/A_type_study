# 로봇청소기 
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
def solve(ci,cj,dr):
    cnt = 0
    while 1:
        arr[ci][cj] = 2
        cnt += 1

        flag = 1
        while flag == 1:
            for nd in ((dr+3)%4, (dr+2)%4, (dr+1)%4, dr):
                ni, nj = ci+di[nd], cj+dj[nd]
                if arr[ni][nj] == 0:
                    ci,cj,dr = ni,nj,nd
                    flag = 0 
                    break
            else: 
                bi,bj = ci-di[dr],cj-dj[dr]
                if arr[bi][bj] == 1:
                    return cnt
                else: 
                    ci,cj = bi,bj

    return -1 

N, M = map(int, input().split())
si, sj, dr = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

ans = solve(si,sj,dr)
print(ans)