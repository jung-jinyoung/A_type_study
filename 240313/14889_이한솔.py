# 스타트와 링크

# 백트레킹 - 가능한 모든 경우
# 입력값 -> 이중리스트 생성
# 조합 사용?
# 진짜 전혀 이해가 안갑니다.. 

def cal(alst,blst):
    asm = bsm = 0
    for i in range(M):
        for j in range(M):
            asm += capa[alst[i]][alst[j]]
            bsm += capa[blst[i]][blst[j]]
    return abs(asm-bsm)

def dfs(n,alst,blst):
    global ans
    if n == N:
        if len(alst)==len(blst): # 같은 인원 수로 팀을 구성
            ans = min(ans,cal(alst,blst))
        return
    # A 팀 선택
    dfs(n+1, alst+[n], blst)
    # B 팀 선택
    dfs(n+1,alst,blst+[n])

N = int(input())
capa = [list(map(int, input().split())) for _ in range(N)]

M = N//2
ans = 100*M*M
dfs(0,[],[])
print(ans)




