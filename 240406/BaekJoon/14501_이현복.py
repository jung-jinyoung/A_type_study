import sys
sys.stdin = open('input1.txt','r')

'''
14501_퇴사
(python/pypy)
 31120/112896kb
 64/148ms
'''
def dfs(day,money,aaa):
    global maxv
    if day== N+1:
        maxv=max(maxv,money)
        return
    if day > N+1:
        maxv=max(maxv,money-aaa)
        return
    for i in range(day,N+1):
        dfs(i+arr[day][0],money+arr[day][1],arr[day][1])
    return

maxv=0
N=int(input())
arr =[[1,0]] + [list(map(int,input().split())) for _ in range(N)]
dfs(0,0,0)
print(maxv)