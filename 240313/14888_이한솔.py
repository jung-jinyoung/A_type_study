# 연산자 끼워넣기
# 가능한 모든 경우를 실행해도 될 것 같은 경우 : 백트레킹

def dfs(i, add, sub, mul, div, s):
    global mx, mn
    if i == N:
        if s > mx:
            mx = s
        if s < mn:
            mn = s
        return

    if add:
        dfs(i + 1, add - 1, sub, mul, div, s + I[i])
    if sub:
        dfs(i + 1, add, sub - 1, mul, div, s - I[i])
    if mul:
        dfs(i + 1, add, sub, mul - 1, div, s * I[i])
    if div:
        dfs(i + 1, add, sub, mul, div - 1, int(s / I[i]))


N = int(input())
I = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

# 1e8 (1*10**8)
mn, mx = int(1e9), int(-1e9)  # min, max 값 초기화
dfs(1, add, sub, mul, div, I[0])
print(mx, mn)

