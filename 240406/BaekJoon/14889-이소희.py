'''
6
0 1 2 3 4 5
1 0 2 3 4 5
1 2 0 3 4 5
1 2 3 0 4 5
1 2 3 4 0 5
1 2 3 4 5 0
'''
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
result = 10 * 50 ** 8

def calc(lst): # lst = [1, 4] 라면 S[1][4] + S[4][1]
    ssum = 0
    for i in range(len(lst)):
        for j in range((len(lst))):
            p = lst[i]
            q = lst[j]
            ssum += S[p][q]
    return ssum

def dfs(i, alst, blst):
    global result
    if result == 0:
        return
    if i == N:
        if len(alst) == len(blst):
        # 두 팀의 능력치 차이 구하기
            result = min(result, abs(calc(alst) - calc(blst)))
        return
    dfs(i+1, alst + [i], blst)
    dfs(i+1, alst, blst+[i])

dfs(0, [], [])
print(result)
