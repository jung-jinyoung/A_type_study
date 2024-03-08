"""
내구도와 무게
계란으로 계란을 치면 각 계란의 내구도는 상대 계란의 무게만큼 깎임
내구도가 0 이하가 되는 순간 깨짐


1. 가장 왼쪽의 계란을 든다

2. 손에 들고 있는 계란으로 깨지지 않은 다른 계란중 하나를 침
    손에 든 계란이 깨지거나 깨지지 않은 다른 계란이 없으면 치지 않고 넘어감
    이후, 손에 근 계란을 원래 자리에 내려놓고 3번 과정을 진행

3. 가장 최근에 든 계란의 한 칸 오른쪽 계란을 손에 들고 2번 과정을 다시 진행.
    단, 가장 최근에 든 계란이 가장 오른쪽에 위치한 계란일 경우 계란을 치는 과정을 종료
"""
def dfs(n, cnt):
    global ans
    if n == N:      # 모든 계란 부딫히기 완료
        ans = max(ans, cnt)
        return

    if arr[n][0] <= 0:  # 현재 계란이 깨진 경우 -> 다음 계란
        dfs(n+1, cnt)
    else:               # 현재 계란이 안깨진 상태
        flag = False    # 한번도 안 부딪혔다면 -> 그래도 다음 계란으로 이동
        for j in range(N):      # 하나씩 부딪치다
            if n==j or arr[j][0] <= 0:
                continue

            flag = True 
            arr[n][0] -= arr[j][1]
            arr[j][0] -= arr[n][1]
            dfs(n+1, cnt+int(arr[n][0] <= 0) + int(arr[j][0] <= 0))

            arr[n][0] += arr[j][1]
            arr[j][0] += arr[n][1]

        if flag == False:   # 여전히 한번도 안부딫혔다면
            dfs(n+1, cnt)


N = int(input())    # 계란 총 개수
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
dfs(0, 0)       # 계란 index, 깨진계란 개수
print(ans)