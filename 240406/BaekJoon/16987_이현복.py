import sys
sys.stdin = open('input1.txt','r')

'''
16987_계란으로 계란치기
(python/pypy)
 31120/121084kb
 3640/988ms
'''

def dfs(now,arr,res):
    global result
    if now == N:
        result = max(result,res)
        return
    if arr[now][0]<=0:
        dfs(now+1,arr,res)
    else:
        check = 1
        for i in range(N):
            if arr[i][0]>0 and now!=i:
                tmp=0
                arr[now][0]-=arr[i][1]      # 깨짐
                arr[i][0]-=arr[now][1]
                if arr[now][0] <= 0: tmp+=1
                if arr[i][0] <= 0: tmp+=1
                dfs(now+1,arr,res+tmp)
                arr[now][0]+=arr[i][1]      # dfs갔으니 복구
                arr[i][0]+=arr[now][1]
                check = 0                   # 계란을 들었으면 계란이라도 깨야하니 체크
        if check:                           # 들고 있는 계란이 유일한 계란
            result = max(result,res) 
        return                              # 들고있는계란이 마지막이거나 있어도 안깬 경우면 리턴
N = int(input())
egg = [list(map(int,input().split())) for _ in range(N)]    # [내구도,무게]
result = 0
dfs(0,egg,0)
print(result)