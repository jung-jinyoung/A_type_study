'''
egg[0] 을 들어
egg[0] 보다 무게가 큰 계란이 나오거나, egg[0]의 내구성이 0이 되면
계란을 바꿔
3
8 5
1 100
3 5
'''
def dfs(index, cnt):
    global ans
    if ans >= (cnt+(N-index)*2):
        return
    
    if index == N:
        ans = max(ans, cnt)
        return
    if egg[index][0] <= 0: #깨진 ㄱㅖ란이라면 다음으로
        dfs(index+1, cnt)
    else:
        flag = False
        for j in range(N):
            if index == j or egg[j][0] <= 0:
                continue
            else:
                flag == True
                #계란 부딪히기
                egg[index][0] -= egg[j][1]
                egg[j][0] -= egg[index][1]
                dfs(index+1, cnt + int(egg[index][0]<= 0) + int(egg[j][0]<= 0))
                egg[index][0] += egg[j][1]
                egg[j][0] += egg[index][1]
            if flag == False:
                dfs(index+1, cnt)
import sys
input = sys.stdin.readline
N = int(input())
egg = [list(map(int, input().split()))for _ in range(N)]
ans = 0
dfs(0,0)
print(ans)