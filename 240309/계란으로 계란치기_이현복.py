# 16987_계란으로 계란치기
'''
https://www.acmicpc.net/problem/16987
'''
def fff(loc,sss):       # loc = 몇번째 location, sss = egg 내구도 
    if loc == N:        # 끝나는 조건
        cnt = 0
        for egg in sss:
            if egg <1:
                cnt+=1
        res.append(cnt)
        return
    elif sss[loc] >0:   # 잡은 계란 내구도 남아있을때
        for i in range(N):
            if i != loc and sss[i]>0:
                aaa=1
                sss[i]-=W[loc]      # 계란치기 결과 반영
                sss[loc]-=W[i]
                fff(loc+1,sss)      # 다음 순번으로 넘어가면서 재귀
                sss[i]+=W[loc]      # 계란치기 결과 복구
                sss[loc]+=W[i]
        else:
            fff(loc+1,sss)
    else:
        fff(loc+1,sss)
N = int(input())
S=[0]*N
W=[0]*N
res=[]
for i in range(N):
    S[i],W[i] = map(int,input().split())
fff(0,S)
print(max(res))